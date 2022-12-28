import sys

from electrickiwi_api.auth import AbstractAuth
from electrickiwi_api.exceptions import AuthException, ApiException
from electrickiwi_api.model import OutageContact, Hop, HopIntervals, ConsumptionSummary, AccountBalance, BillFile, \
    Bills, Bill, BillingFrequency, BillingAddress, CustomerConnection, Customer, Session

from electrickiwi_api.model import ConsumptionAverage


class ElectricKiwiEndpoint:
    # scope read_customer_detail
    customer = "/customer/{customerNumber}/"
    # scope read_connection_detail
    customerConnectionDetails = "/connection/details/{customerNumber}/{connectionId}/"
    # scope read_billing_address
    billingAddress = "/billing/address/{customerNumber}/"
    # scope read_billing_frequency
    billingFrequency = "/billing/frequency/{customerNumber}/"
    # scope read_billing_bills
    billingBills = "/billing/bills/{customerNumber}/?limit={limit}&offset={offset}/"
    # scope read_billing_bill
    billingBill = "/billing/bill/{customerNumber}/{billId}/"
    # scope read_billing_bill_file
    billingBillFile = "/billing/bill/file/{customerNumber}/{billId}/"
    # scope read_account_running_balance
    accountBalance = "/account/running_balance/{customerNumber}/"
    # scope read_consumption_summary
    consumptionSummary = "/consumption/summary/{customerNumber}/{connectionId}/?start_date={startDate}&end_date={" \
                         "endDate} "
    # scope read_consumption_averages
    consumptionAverages = "/consumption/averages/{customerNumber}/{connectionId}/?start_date={startDate}&end_date={" \
                          "endDate}&group_by={groupBy} "
    # scope read_hop_intervals_config
    hourOfPowerIntervals = "/hop/"
    # scope read_hop_connection, save_hop_connection (POST) (hour of power)
    hourOfPowerByConnection = "/hop/{customerNumber}/{connectionId}/"
    # scope read_outage_contact
    outageContactInformationForConnection = "/service/outage/contact/{connectionId}/"
    # read_session
    session = "/session/"


def get_next_page(response):
    return {
        "limit": response["meta"]["pagination"]["limit"],
        "offset": response["meta"]["pagination"]["offset"] + response["meta"]["pagination"]["limit"],
    }


def check_status(status):
    if status == 401:
        raise AuthException(f"Authorization failed: {status}")
    if status != 200:
        raise ApiException(f"Error request failed: {status}")


class ElectricKiwiApi:

    def __init__(self, auth: AbstractAuth):
        self.connection_id = None
        self.customer_number = None
        self.auth = auth

    async def set_active_session(self):
        resp = await self.auth.request("get", ElectricKiwiEndpoint.session)
        check_status(resp.status)

        customer_session = Session.from_dict(await resp.json())
        self.customer_number = customer_session.customer[0].customer_number
        self.connection_id = customer_session.customer[0].connection.connection_id

    async def get_active_session(self):
        session = await self.auth.request("get", ElectricKiwiEndpoint.session)
        check_status(session.status)
        return Session.from_dict(await session.json())

    async def get_customer(self):
        customer = await self.auth.request("get",
                                           ElectricKiwiEndpoint.customer.format(customerNumber=self.customer_number))
        check_status(customer.status)
        return Customer.from_dict(await customer.json())

    async def get_connection_details(self):
        connection_details = await self.auth.request("get", ElectricKiwiEndpoint.customerConnectionDetails.format(
            customerNumber=self.customer_number,
            connectionId=self.connection_id))
        check_status(connection_details.status)
        return CustomerConnection.from_dict(await connection_details.json())

    async def get_billing_address(self):
        billing_address = await self.auth.request("get",
                                                  ElectricKiwiEndpoint.billingAddress.format(
                                                      customerNumber=self.customer_number))
        check_status(billing_address.status)
        return BillingAddress.from_dict(await billing_address.json())

    async def get_billing_frequency(self):
        billing_frequency = await self.auth.request("get", ElectricKiwiEndpoint.billingFrequency.format(
            customerNumber=self.customer_number))
        check_status(billing_frequency.status)
        return BillingFrequency.from_dict(await billing_frequency.json())

    # @paginated(by_query_params=get_next_page)
    async def get_billing_bills(self, limit = 5, offset = 0):
        billing_bills = await self.auth.request("get", ElectricKiwiEndpoint.billingBills.format(customerNumber=self.customer_number, limit=limit, offset=offset))
        check_status(billing_bills.status)
        return Bills.from_dict(await billing_bills.json())

    async def get_billing_bill(self, bill_id):
        billing_bill = await self.auth.request("get",
                                               ElectricKiwiEndpoint.billingBill.format(
                                                   customerNumber=self.customer_number,
                                                   billId=bill_id))
        check_status(billing_bill.status)
        return Bill.from_dict(await billing_bill.json())

    async def get_bill_file(self, bill_id):
        bill_file = await self.auth.request("get",
                                            ElectricKiwiEndpoint.billingBillFile.format(
                                                customerNumber=self.customer_number,
                                                billId=bill_id))
        check_status(bill_file.status)
        return BillFile.from_dict(await bill_file.json())

    async def get_account_balance(self):
        account_balance = await self.auth.request("get",
                                                  ElectricKiwiEndpoint.accountBalance.format(
                                                      customerNumber=self.customer_number))
        check_status(account_balance.status)
        return AccountBalance.from_dict(await account_balance.json())

    async def get_consumption_summary(self, start_date, end_date):
        consumption_summary = await self.auth.request("get", ElectricKiwiEndpoint.consumptionSummary.format(
            customerNumber=self.customer_number,
            connectionId=self.connection_id),
                                                      json={start_date: start_date, end_date: end_date})
        check_status(consumption_summary.status)
        return ConsumptionSummary.from_dict(await consumption_summary.json())

    async def get_consumption_averages(self, start_date, end_date, group_by="week"):
        consumption_average = await self.auth.request("get", ElectricKiwiEndpoint.consumptionAverages.format(
            customerNumber=self.customer_number,
            connectionId=self.connection_id),
                                                      json={start_date: start_date, end_date: end_date,
                                                            group_by: group_by})
        check_status(consumption_average.status)
        return ConsumptionAverage.from_dict(await consumption_average.json())

    async def get_hop_intervals(self):
        hop_intervals = await self.auth.request("get", ElectricKiwiEndpoint.hourOfPowerIntervals)
        check_status(hop_intervals.status)
        return HopIntervals.from_dict(await hop_intervals.json())

    async def get_hop(self):
        get_hop = await self.auth.request("get", ElectricKiwiEndpoint.hourOfPowerByConnection.format(
            customerNumber=self.customer_number,
            connectionId=self.connection_id))
        check_status(get_hop.status)
        return Hop.from_dict(await get_hop.json())

    async def post_hop(self, hop_interval):
        data = {"start": hop_interval}
        post_hop = await self.auth.request("post", ElectricKiwiEndpoint.hourOfPowerByConnection.format(
            customerNumber=self.customer_number,
            connectionId=self.connection_id),
                                           json=data)
        check_status(post_hop.status)
        return Hop.from_dict(await post_hop.json())

    async def get_outage_info(self):
        outage_info = await self.auth.request("get",
                                              ElectricKiwiEndpoint.outageContactInformationForConnection.format(
                                                  connectionId=self.connection_id))
        check_status(outage_info.status)
        return OutageContact.from_dict(await outage_info.json())

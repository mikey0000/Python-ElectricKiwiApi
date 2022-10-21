import os

from typing import Type, Optional

from src.electrickiwi_api.auth import AbstractAuth


class ElectricKiwiEndpoint:
    # scope read_customer_detail
    customer = "customer/{customerNumber}/"
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


class ElectricKiwiApi:

    def __init__(self, auth: AbstractAuth):
        self.connection_id = None
        self.customer_number = None
        self.auth = auth
        self.set_active_session()

    def set_active_session(self):
        customer_session = await self.auth.request("get", ElectricKiwiEndpoint.session)
        self.customer_number = customer_session["data"]["customer"][0]["customer_number"]
        self.connection_id = customer_session["data"]["customer"][0]["connection"]["connection_id"]

    def get_active_session(self):
        await self.auth.request("get", ElectricKiwiEndpoint.session)

    def get_customer(self):
        await self.auth.request("get", ElectricKiwiEndpoint.customer.format(customerNumber=self.customer_number))

    def get_connection_details(self):
        await self.auth.request("get", ElectricKiwiEndpoint.customerConnectionDetails.format(
            customerNumber=self.customer_number,
            connectionId=self.connection_id))

    def get_billing_address(self):
        await self.auth.request("get",
                                ElectricKiwiEndpoint.billingAddress.format(customerNumber=self.customer_number))

    def get_billing_frequency(self):
        await self.auth.request("get", ElectricKiwiEndpoint.billingFrequency.format(
            customerNumber=self.customer_number))

    # @paginated(by_query_params=get_next_page)
    def get_billing_bills(self):
        await self.auth.request("get", ElectricKiwiEndpoint.billingBills)

    def get_billing_bill(self, bill_id):
        await self.auth.request("get",
                                ElectricKiwiEndpoint.billingBill.format(customerNumber=self.customer_number,
                                                                        billId=bill_id))

    def get_bill_file(self, bill_id):
        await self.auth.request("get",
                                ElectricKiwiEndpoint.billingBillFile.format(customerNumber=self.customer_number,
                                                                            billId=bill_id))

    def get_account_balance(self):
        await self.auth.request("get",
                                ElectricKiwiEndpoint.accountBalance.format(customerNumber=self.customer_number))

    def get_consumption_summary(self, start_date, end_date):
        await self.auth.request("get", ElectricKiwiEndpoint.consumptionSummary.format(
            customerNumber=self.customer_number,
            connectionId=self.connection_id),
                                json={start_date: start_date, end_date: end_date})

    def get_consumption_averages(self, start_date, end_date, group_by="week"):
        await self.auth.request("get", ElectricKiwiEndpoint.consumptionAverages.format(
            customerNumber=self.customer_number,
            connectionId=self.connection_id),
                                json={start_date: start_date, end_date: end_date, group_by: group_by})

    def get_hop_intervals(self):
        await self.auth.request("get", ElectricKiwiEndpoint.hourOfPowerIntervals)

    def get_hop(self):
        await self.auth.request("get", ElectricKiwiEndpoint.hourOfPowerByConnection.format(
            customerNumber=self.customer_number,
            connectionId=self.connection_id))

    def post_hop(self, hop_interval):
        data = {"start": hop_interval}
        await self.auth.request("post", ElectricKiwiEndpoint.hourOfPowerByConnection.format(
            customerNumber=self.customer_number,
            connectionId=self.connection_id),
                                json=data)

    def get_outage_info(self):
        await self.auth.request("get",
                                ElectricKiwiEndpoint.outageContactInformationForConnection.format(
                                    connectionId=self.connection_id))

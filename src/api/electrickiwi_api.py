import os

from apiclient import (
    APIClient,
    endpoint,
    paginated
)

@endpoint(base_url=os.environ["ELECTRICKIWI_BASE_URL"])
class ElectricKiwiEndpoint:
    # scope read_customer_detail
    customer = "customer/{customerNumber}"
    # scope read_connection_detail
    customerConnectionDetails = "/connection/details/{customerNumber}/{connectionId}/"
    # scope read_billing_address
    billingAddress = "/billing/address/{customerNumber}"
    # scope read_billing_frequency
    billingFrequency = "/billing/frequency/{customerNumber}"
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
    session = "/session"


def get_next_page(response):
    return {
        "limit": response["meta"]["pagination"]["limit"],
        "offset": response["meta"]["pagination"]["offset"] + response["meta"]["pagination"]["limit"],
    }


class ElectricKiwiApi(APIClient):

    def __init__(self):
        super().__init__()
        # token etc
        customer_session = self.get_session()
        self.customer_number = customer_session.data.customer.customer_number
        self.connection_id = customer_session.data.customer.connection.connection_id

    def get_session(self):
        return self.get(ElectricKiwiEndpoint.session)

    def get_customer(self):
        return self.get(ElectricKiwiEndpoint.customer.format(customerNumber=self.customer_number))

    def get_connection_details(self):
        return self.get(ElectricKiwiEndpoint.customerConnectionDetails.format(customerNumber=self.customer_number,
                                                                              connectionId=self.connection_id))

    def get_billing_address(self):
        return self.get(ElectricKiwiEndpoint.billingAddress.format(customerNumber=self.customer_number))

    def get_billing_frequency(self):
        return self.get(ElectricKiwiEndpoint.billingFrequency.format(customerNumber=self.customer_number))

    @paginated(by_query_params=get_next_page)
    def get_billing_bills(self):
        return self.get(ElectricKiwiEndpoint.billingBills)

    def get_billing_bill(self, bill_id):
        return self.get(ElectricKiwiEndpoint.billingBill.format(customerNumber=self.customer_number, billId=bill_id))

    def get_bill_file(self, bill_id):
        return self.get(
            ElectricKiwiEndpoint.billingBillFile.format(customerNumber=self.customer_number, billId=bill_id))

    def get_account_balance(self):
        return self.get(ElectricKiwiEndpoint.accountBalance.format(customerNumber=self.customer_number))

    def get_consumption_summary(self, start_date, end_date):
        return self.get(ElectricKiwiEndpoint.consumptionSummary.format(customerNumber=self.customer_number,
                                                                       connectionId=self.connection_id),
                        {start_date: start_date, end_date: end_date})

    def get_consumption_averages(self, start_date, end_date, group_by="week"):
        return self.get(ElectricKiwiEndpoint.consumptionAverages.format(customerNumber=self.customer_number,
                                                                        connectionId=self.connection_id),
                        {start_date: start_date, end_date: end_date, group_by: group_by})

    def get_hop_intervals(self):
        return self.get(ElectricKiwiEndpoint.hourOfPowerIntervals)

    def get_hop(self):
        return self.get(ElectricKiwiEndpoint.hourOfPowerByConnection.format(customerNumber=self.customer_number,
                                                                            connectionId=self.connection_id))

    def post_hop(self, hop_interval):
        data = {"start": hop_interval}
        return self.post(ElectricKiwiEndpoint.hourOfPowerByConnection.format(customerNumber=self.customer_number,
                                                                             connectionId=self.connection_id),data=data)

    def get_outage_info(self):
        return self.get(ElectricKiwiEndpoint.outageContactInformationForConnection.format(connectionId=self.connection_id))

from typing import List
from typing import Any

from dataclasses import dataclass


@dataclass
class Summary:
    credits: str
    electricity_used: str
    other_charges: str
    payments: str

    @staticmethod
    def from_dict(obj: dict) -> 'Summary':
        _credits = str(obj.get("credits"))
        _electricity_used = str(obj.get("electricity_used"))
        _other_charges = str(obj.get("other_charges"))
        _payments = str(obj.get("payments"))
        return Summary(_credits, _electricity_used, _other_charges, _payments)


@dataclass
class AccountBalanceConnection:
    hop_percentage: str
    id: int
    running_balance: str
    start_date: str
    unbilled_days: int

    @staticmethod
    def from_dict(obj: Any) -> 'AccountBalanceConnection':
        _hop_percentage = str(obj.get("hop_percentage"))
        _id = int(obj.get("id"))
        _running_balance = str(obj.get("running_balance"))
        _start_date = str(obj.get("start_date"))
        _unbilled_days = int(obj.get("unbilled_days"))
        return AccountBalanceConnection(_hop_percentage, _id, _running_balance, _start_date, _unbilled_days)


@dataclass
class AccountBalance:
    connections: List[AccountBalanceConnection]
    last_billed_amount: str
    last_billed_date: str
    next_billing_date: str
    is_prepay: str
    summary: Summary
    total_account_balance: str
    total_billing_days: int
    total_running_balance: str
    type: str

    @staticmethod
    def from_dict(account_balance_data: dict) -> 'AccountBalance':
        account_balance = account_balance_data.get("data")

        _connections = [AccountBalanceConnection.from_dict(y) for y in account_balance.get("connections")]
        _last_billed_amount = str(account_balance.get("last_billed_amount"))
        _last_billed_date = str(account_balance.get("last_billed_date"))
        _next_billing_date = str(account_balance.get("next_billing_date"))
        _is_prepay = str(account_balance.get("is_prepay"))
        _summary = Summary.from_dict(account_balance.get("summary"))
        _total_account_balance = str(account_balance.get("total_account_balance"))
        _total_billing_days = int(account_balance.get("total_billing_days"))
        _total_running_balance = str(account_balance.get("total_running_balance"))
        _type = str(account_balance.get("type"))
        return AccountBalance(_connections, _last_billed_amount, _last_billed_date, _next_billing_date, _is_prepay,
                              _summary, _total_account_balance, _total_billing_days, _total_running_balance, _type)


@dataclass
class Customer:
    bill_address_1: str
    bill_address_2: str
    bill_city: str
    bill_company: str
    bill_name: str
    bill_post_code: str
    birth_date: str
    customer_number: int
    email: str
    first_name: str
    last_name: str
    middle_name: str
    phone_number: str
    gender: str
    is_active: str
    medically_dependent_customer: str

    @staticmethod
    def from_dict(customer_data: dict) -> 'Customer':
        customer = customer_data.get("data")

        _bill_address_1 = str(customer.get("bill_address_1"))
        _bill_address_2 = str(customer.get("bill_address_2"))
        _bill_city = str(customer.get("bill_city"))
        _bill_company = str(customer.get("bill_company"))
        _bill_name = str(customer.get("bill_name"))
        _bill_post_code = str(customer.get("bill_post_code"))
        _birth_date = str(customer.get("birth_date"))
        _customer_number = int(customer.get("customer_number"))
        _email = str(customer.get("email"))
        _first_name = str(customer.get("first_name"))
        _last_name = str(customer.get("last_name"))
        _middle_name = str(customer.get("middle_name"))
        _phone_number = str(customer.get("phone_number"))
        _gender = str(customer.get("gender"))
        _is_active = str(customer.get("is_active"))
        _medically_dependent_customer = str(customer.get("medically_dependent_customer"))
        return Customer(_bill_address_1, _bill_address_2, _bill_city, _bill_company, _bill_name, _bill_post_code,
                        _birth_date, _customer_number, _email, _first_name, _last_name, _middle_name, _phone_number,
                        _gender, _is_active, _medically_dependent_customer)


@dataclass
class Hop:
    start_time: str
    end_time: str
    interval_start: str
    interval_end: str

    @staticmethod
    def from_dict(obj: Any) -> 'Hop':
        _start_time = str(obj.get("start_time"))
        _end_time = str(obj.get("end_time"))
        _interval_start = str(obj.get("interval_start"))
        _interval_end = str(obj.get("interval_end"))
        return Hop(_start_time, _end_time, _interval_start, _interval_end)


@dataclass
class CustomerConnection:
    type: str
    id: int
    customer_number: int
    identifier: str
    address: str
    is_active: str
    hop: Hop
    start_date: str
    end_date: str

    @staticmethod
    def from_dict(customer_connection_data: Any) -> 'CustomerConnection':
        customer_connection = customer_connection_data.get("data")

        _type = str(customer_connection.get("type"))
        _id = int(customer_connection.get("id"))
        _customer_number = int(customer_connection.get("customer_number"))
        _identifier = str(customer_connection.get("identifier"))
        _address = str(customer_connection.get("address"))
        _is_active = str(customer_connection.get("is_active"))
        _hop = Hop.from_dict(customer_connection.get("hop"))
        _start_date = str(customer_connection.get("start_date"))
        _end_date = str(customer_connection.get("end_date"))
        return CustomerConnection(_type, _id, _customer_number, _identifier, _address, _is_active, _hop, _start_date,
                                  _end_date)


@dataclass
class BillingAddress:
    address_1: str
    address_2: str
    city: str
    company: str
    name: str
    post_code: str
    type: str

    @staticmethod
    def from_dict(billing_address_data: dict) -> 'BillingAddress':
        billing_address = billing_address_data.get("data")

        _address_1 = str(billing_address.get("address_1"))
        _address_2 = str(billing_address.get("address_2"))
        _city = str(billing_address.get("city"))
        _company = str(billing_address.get("company"))
        _name = str(billing_address.get("name"))
        _post_code = str(billing_address.get("post_code"))
        _type = str(billing_address.get("type"))
        return BillingAddress(_address_1, _address_2, _city, _company, _name, _post_code, _type)


@dataclass
class BillingFrequency:
    billing_date: str
    day: str
    frequency: str
    period: str
    type: str

    @staticmethod
    def from_dict(billing_frequency_data: dict) -> 'BillingFrequency':
        billing_frequency = billing_frequency_data.get("data")
        _billing_date = str(billing_frequency.get("billing_date"))
        _day = str(billing_frequency.get("day"))
        _frequency = str(billing_frequency.get("frequency"))
        _period = str(billing_frequency.get("period"))
        _type = str(billing_frequency.get("type"))
        return BillingFrequency(_billing_date, _day, _frequency, _period, _type)


@dataclass
class Bill:
    date_to_pay: str
    date_generated: str
    end_date: str
    file: str
    id: int
    invoice_total_charges_incl_gst: float
    start_date: str
    status: str
    status_message: str
    title: str
    total_to_pay: float
    type: str

    @staticmethod
    def from_dict(bill_data: Any) -> 'Bill':
        bill = bill_data.get("data")
        if bill is None:
            bill = bill_data

        _date_to_pay = str(bill.get("date_to_pay"))
        _date_generated = str(bill.get("date_generated"))
        _end_date = str(bill.get("end_date"))
        _file = str(bill.get("file"))
        _id = int(bill.get("id"))
        _invoice_total_charges_incl_gst = float(bill.get("invoice_total_charges_incl_gst"))
        _start_date = str(bill.get("start_date"))
        _status = str(bill.get("status"))
        _status_message = str(bill.get("status_message"))
        _title = str(bill.get("title"))
        _total_to_pay = float(bill.get("total_to_pay"))
        _type = str(bill.get("type"))
        return Bill(_date_to_pay, _date_generated, _end_date, _file, _id, _invoice_total_charges_incl_gst, _start_date,
                    _status, _status_message, _title, _total_to_pay, _type)


@dataclass
class Links:
    first: str
    last: str
    next: str
    previous: str
    self: str

    @staticmethod
    def from_dict(obj: Any) -> 'Links':
        _first = str(obj.get("first"))
        _last = str(obj.get("last"))
        _next = str(obj.get("next"))
        _previous = str(obj.get("previous"))
        _self = str(obj.get("self"))
        return Links(_first, _last, _next, _previous, _self)


@dataclass
class Pagination:
    limit: int
    links: Links
    offset: int
    page_count: int
    total_count: int

    @staticmethod
    def from_dict(obj: Any) -> 'Pagination':
        _limit = int(obj.get("limit"))
        _links = Links.from_dict(obj.get("links"))
        _offset = int(obj.get("offset"))
        _page_count = int(obj.get("page_count"))
        _total_count = int(obj.get("total_count"))
        return Pagination(_limit, _links, _offset, _page_count, _total_count)


@dataclass
class Meta:
    pagination: Pagination

    @staticmethod
    def from_dict(obj: Any) -> 'Meta':
        _pagination = Pagination.from_dict(obj.get("pagination"))
        return Meta(_pagination)


@dataclass
class Bills:
    bills: List[Bill]
    meta: Meta
    type: str

    @staticmethod
    def from_dict(bills_data: dict) -> 'Bills':
        bills = bills_data.get('data')

        _bills = [Bill.from_dict(y) for y in bills.get("bills")]
        _meta = Meta.from_dict(bills.get("meta"))
        _type = str(bills.get("type"))
        return Bills(_bills, _meta, _type)


@dataclass
class BillFile:
    file_base64: str
    file_name: str
    id: int
    type: str

    @staticmethod
    def from_dict(bill_file_data: dict) -> 'BillFile':
        bill_file = bill_file_data.get("data")
        _file_base64 = str(bill_file.get("file_base64"))
        _file_name = str(bill_file.get("file_name"))
        _id = int(bill_file.get("id"))
        _type = str(bill_file.get("type"))
        return BillFile(_file_base64, _file_name, _id, _type)


@dataclass
class Range:
    end_date: str
    start_date: str

    @staticmethod
    def from_dict(obj: Any) -> 'Range':
        _end_date = str(obj.get("end_date"))
        _start_date = str(obj.get("start_date"))
        return Range(_end_date, _start_date)


@dataclass
class UsageCharge:
    end_date: str
    fixed_rate_incl_gst: str
    hop_saving: str
    start_date: str
    supply_days: int
    total_consumption: str
    total_fixed_charges_incl_gst: str
    total_variable_charges_incl_gst: str
    variable_rate_incl_gst: str

    @staticmethod
    def from_dict(obj: Any) -> 'UsageCharge':
        _end_date = str(obj.get("end_date"))
        _fixed_rate_incl_gst = str(obj.get("fixed_rate_incl_gst"))
        _hop_saving = str(obj.get("hop_saving"))
        _start_date = str(obj.get("start_date"))
        _supply_days = int(obj.get("supply_days"))
        _total_consumption = str(obj.get("total_consumption"))
        _total_fixed_charges_incl_gst = str(obj.get("total_fixed_charges_incl_gst"))
        _total_variable_charges_incl_gst = str(obj.get("total_variable_charges_incl_gst"))
        _variable_rate_incl_gst = str(obj.get("variable_rate_incl_gst"))
        return UsageCharge(_end_date, _fixed_rate_incl_gst, _hop_saving, _start_date, _supply_days, _total_consumption,
                           _total_fixed_charges_incl_gst, _total_variable_charges_incl_gst, _variable_rate_incl_gst)


@dataclass
class ConsumptionSummary:
    range: Range
    usage_charges: List[UsageCharge]
    type: str

    @staticmethod
    def from_dict(consumption_summary_data: Any) -> 'ConsumptionSummary':
        consumption_summary = consumption_summary_data.get("data")
        _range = Range.from_dict(consumption_summary.get("range"))
        _usage_charges = [UsageCharge.from_dict(y) for y in consumption_summary.get("usage_charges")]
        _type = str(consumption_summary.get("type"))
        return ConsumptionSummary(_range, _usage_charges, _type)


# HOP

@dataclass
class Interval:
    consumption: str
    hop_best: int
    time: str

    @staticmethod
    def from_dict(obj: Any) -> 'Interval':
        _consumption = str(obj.get("consumption"))
        _hop_best = int(obj.get("hop_best"))
        _time = str(obj.get("time"))
        return Interval(_consumption, _hop_best, _time)


@dataclass
class Usage:
    adjustment_charges_incl_gst: str
    bill_consumption: str
    consumption: str
    consumption_adjustment: str
    fixed_charges_excl_gst: str
    fixed_charges_incl_gst: str
    intervals: List[dict]
    percent_consumption_adjustment: str
    range: Range
    status: str
    total_charges_incl_gst: str
    type: str
    variable_charges_excl_gst: str
    variable_charges_incl_gst: str

    @staticmethod
    def from_dict(usage: dict) -> 'Usage':
        _adjustment_charges_incl_gst = str(usage.get("adjustment_charges_incl_gst"))
        _bill_consumption = str(usage.get("bill_consumption"))
        _consumption = str(usage.get("consumption"))
        _consumption_adjustment = str(usage.get("consumption_adjustment"))
        _fixed_charges_excl_gst = str(usage.get("fixed_charges_excl_gst"))
        _fixed_charges_incl_gst = str(usage.get("fixed_charges_incl_gst"))
        _intervals = [{y: [Usage.from_dict(usage.get("intervals").get(y))]} for y in
                      usage.get("usage").keys()]
        _percent_consumption_adjustment = str(usage.get("percent_consumption_adjustment"))
        _range = Range.from_dict(usage.get("range"))
        _status = str(usage.get("status"))
        _total_charges_incl_gst = str(usage.get("total_charges_incl_gst"))
        _type = str(usage.get("type"))
        _variable_charges_excl_gst = str(usage.get("variable_charges_excl_gst"))
        _variable_charges_incl_gst = str(usage.get("variable_charges_incl_gst"))
        return Usage(_adjustment_charges_incl_gst, _bill_consumption, _consumption, _consumption_adjustment,
                     _fixed_charges_excl_gst, _fixed_charges_incl_gst, _intervals, _percent_consumption_adjustment,
                     _range, _status, _total_charges_incl_gst, _type, _variable_charges_excl_gst,
                     _variable_charges_incl_gst)


@dataclass
class Range:
    end_date: str
    start_date: str
    group_by: str

    @staticmethod
    def from_dict(obj: Any) -> 'Range':
        _end_date = str(obj.get("end_date"))
        _start_date = str(obj.get("start_date"))
        _group_by = str(obj.get("group_by"))
        return Range(_end_date, _start_date, _group_by)


@dataclass
class ConsumptionAverage:
    group_breakdown: List[str]
    range: Range
    type: str
    usage: List[dict]

    @staticmethod
    def from_dict(consumption_average_data: dict) -> 'ConsumptionAverage':
        consumption_average = consumption_average_data.get("data")
        _group_breakdown = consumption_average.get("group_breakdown")
        _range = Range.from_dict(consumption_average.get("range"))
        _type = str(consumption_average.get("type"))
        _usage = [{y: [Usage.from_dict(consumption_average.get("usage").get(y))]} for y in
                  consumption_average.get("usage").keys()]
        return ConsumptionAverage(_group_breakdown, _range, _type, _usage)


@dataclass
class HopInterval:
    active: int
    end_time: str
    start_time: str

    @staticmethod
    def from_dict(obj: Any) -> 'HopInterval':
        _active = int(obj.get("active"))
        _end_time = str(obj.get("end_time"))
        _start_time = str(obj.get("start_time"))
        return HopInterval(_active, _end_time, _start_time)


@dataclass
class HopIntervals:
    hop_duration: str
    type: str
    intervals: List[dict]

    @staticmethod
    def from_dict(hop_intervals_data: Any) -> 'HopIntervals':
        hop_intervals = hop_intervals_data.get("data")
        _hop_duration = str(hop_intervals.get("hop_duration"))
        _type = str(hop_intervals.get("type"))
        _intervals = [{y: [HopInterval.from_dict(hop_intervals.get("intervals").get(y))]} for y in
                      hop_intervals.get("intervals").keys()]
        return HopIntervals(_hop_duration, _type, _intervals)


@dataclass
class End:
    end_time: str
    interval: str

    @staticmethod
    def from_dict(obj: Any) -> 'End':
        _end_time = str(obj.get("end_time"))
        _interval = str(obj.get("interval"))
        return End(_end_time, _interval)


@dataclass
class Start:
    start_time: str
    interval: str

    @staticmethod
    def from_dict(obj: Any) -> 'Start':
        _start_time = str(obj.get("start_time"))
        _interval = str(obj.get("interval"))
        return Start(_start_time, _interval)


@dataclass
class Hop:
    connection_id: str
    customer_number: int
    end: End
    start: Start
    type: str

    @staticmethod
    def from_dict(hop_data: Any) -> 'Hop':
        hop = hop_data.get("data")
        _connection_id = str(hop.get("connection_id"))
        _customer_number = int(hop.get("customer_number"))
        _end = End.from_dict(hop.get("end"))
        _start = Start.from_dict(hop.get("start"))
        _type = str(hop.get("type"))
        return Hop(_connection_id, _customer_number, _end, _start, _type)


@dataclass
class Connection:
    address: str
    identifier: str
    connection_id: int

    @staticmethod
    def from_dict(obj: Any) -> 'Connection':
        _address = str(obj.get("address"))
        _identifier = str(obj.get("identifier"))
        _connection_id = int(obj.get("connection_id"))
        return Connection(_address, _identifier, _connection_id)


@dataclass
class Subscriptions:
    bill_alert: str
    stay_ahead: str

    @staticmethod
    def from_dict(obj: Any) -> 'Subscriptions':
        _bill_alert = str(obj.get("bill_alert"))
        _stay_ahead = str(obj.get("stay_ahead"))
        return Subscriptions(_bill_alert, _stay_ahead)


@dataclass
class SessionCustomer:
    connection: Connection
    customer_number: int
    email: str
    first_name: str
    last_name: str
    is_active: str
    subscriptions: Subscriptions

    @staticmethod
    def from_dict(customer: Any) -> 'SessionCustomer':
        _connection = Connection.from_dict(customer.get("connection"))
        _customer_number = int(customer.get("customer_number"))
        _email = str(customer.get("email"))
        _first_name = str(customer.get("first_name"))
        _last_name = str(customer.get("last_name"))
        _is_active = str(customer.get("is_active"))
        _subscriptions = Subscriptions.from_dict(customer.get("subscriptions"))
        return SessionCustomer(_connection, _customer_number, _email, _first_name, _last_name, _is_active, _subscriptions)



@dataclass
class Session:
    customer: List[Customer]
    customer_numbers: List[int]
    type: str

    @staticmethod
    def from_dict(session_data: Any) -> 'Session':
        session = session_data.get("data")
        _customer = [SessionCustomer.from_dict(y) for y in session.get("customer")]
        _customer_numbers = session.get("customer_numbers")
        _type = str(session.get("type"))
        return Session(_customer, _customer_numbers, _type)


@dataclass
class OutageContact:
    message: str
    network_name: str
    outage_url: str
    phone_number: str
    type: str

    @staticmethod
    def from_dict(outage_contact_data: Any) -> 'OutageContact':
        outage_contact = outage_contact_data.get("data")
        _message = str(outage_contact.get("message"))
        _network_name = str(outage_contact.get("network_name"))
        _outage_url = str(outage_contact.get("outage_url"))
        _phone_number = str(outage_contact.get("phone_number"))
        _type = str(outage_contact.get("type"))
        return OutageContact(_message, _network_name, _outage_url, _phone_number, _type)

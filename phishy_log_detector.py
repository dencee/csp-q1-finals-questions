TRUSTED_DOMAINS = [
    "great_company.com",
    "great_company_mail_srvr.com",
    "great_company_partner.com",
    "mailserver.com",
    "travelerhelper.com",
    "fishtankmonitors.com",
    "payroll.com",
    "great_food.com",
    "restaurant_reservations.com",
    "bestofficesupplies.com",
    "campingsupplies.com",
    "campingreservations.com"
]

def scan_log(file_name):
  log_file = open(file_name, "r")
  for line in log_file:
    print(line)

    # Code your pHishy algorithm here (ok, I'll stop with the puns now)



print(scan_log("email_record.log"))
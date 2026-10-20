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
  line_num = 0
  sus_domains = []
  log_file = open(file_name, "r")
  for line in log_file:
    line_num += 1

    http_index = line.find("http://")
    if(http_index != -1):
      domain_index = http_index + len("http://")
      domain = ""
      while(line[domain_index] != "."):
        domain += line[domain_index]
        domain_index += 1

      #domain = domain + line[domain_index] + line[domain_index + 1] + line[domain_index + 2] + line[domain_index + 3]
      domain = [domain + line[domain_index + i] for i in range(4)]
      if domain.lower() not in TRUSTED_DOMAINS:
        print(domain)
        sus_domains.append(f'{line_num}. {domain}')

  return sus_domains
    # Code your pHishy algorithm here (ok, I'll stop with the puns now)



print(scan_log("email_record.log"))
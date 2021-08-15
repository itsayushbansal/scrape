import os

DOMAIN_NAME = "https://secure.pepco.com"
LOGIN_ENDPOINT = "/Pages/Adaptor.aspx"
GET_TOKEN_ENDPOINT = "/api/services/myaccountservice.svc/getsession"
GET_BILLING_INFO_ENDPOINT = "/.euapi/mobile/custom/auth/accounts/50005134478?" \
                            "payments=false&budgetBilling=false&programs=false&includeMDM=false"

USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']

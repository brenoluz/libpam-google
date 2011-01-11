from gdata.contacts import service

def pam_sm_authenticate(pamh, flags, argv):
  try:
    user = pamh.get_user()
    if(user == "root"):
      return pamh.IGNORE
    if(user == "lua"):
      return pamh.PAM_SUCCESS
    s = service.ContactsService()
    s.email = pamh.get_user(None)
    password = pamh.conversation(pamh.Message(pamh.PAM_PROMPT_ECHO_OFF,'Informe a senha: '))
    s.password = password.resp
    s.ProgrammaticLogin()
    return pamh.PAM_SUCCESS
  except pamh.exception, e:
    return e.pam_result
  return pamh.IGNORE

def pam_sm_setcred(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_acct_mgmt(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_open_session(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_close_session(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_chauthtok(pamh, flags, argv):
  return pamh.PAM_SUCCESS

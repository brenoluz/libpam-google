#
# Duplicates pam_permit.c
#
import pdb
import getpass
from gdata.contacts import service
DEFAULT_USER	= "nobody"

def pam_sm_authenticate(pamh, flags, argv):
  try:
    user = pamh.get_user(None)	
    if(user == "marxluz"):	
      s = service.ContactsService()
      s.email = user
      s.password = getpass.getpass()
      s.ProgrammaticLogin()
      pamh.user = "breno"
      return pamh.PAM_SUCCESS
    else:
      return pamh.PAM_IGNORE
  except pamh.exception, e:
    return e.pam_result

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

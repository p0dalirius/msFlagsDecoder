#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : msFlagsDecoder.py
# Author             : Podalirius (@podalirius_)
# Date created       : 13 Oct 2021

import argparse
from enum import Enum

## Data

class userAccountControl(Enum):
    # https://docs.microsoft.com/en-us/troubleshoot/windows-server/identity/useraccountcontrol-manipulate-account-properties#property-flag-descriptions
    SCRIPT                         = (0b00000000000000000000000000000001, "The logon script will be run.")
    ACCOUNTDISABLE                 = (0b00000000000000000000000000000010, "The user account is disabled.")
    RESERVED_B02                   = (0b00000000000000000000000000000100, "Reserved bit 02")
    HOMEDIR_REQUIRED               = (0b00000000000000000000000000001000, "The home folder is required.")
    LOCKOUT                        = (0b00000000000000000000000000010000, "Account locked out.")
    PASSWD_NOTREQD                 = (0b00000000000000000000000000100000, "No password is required.")
    PASSWD_CANT_CHANGE             = (0b00000000000000000000000001000000, "The user can't change the password. It's a permission on the user's object.")
    ENCRYPTED_TEXT_PWD_ALLOWED     = (0b00000000000000000000000010000000, "The user can send an encrypted password.")
    TEMP_DUPLICATE_ACCOUNT         = (0b00000000000000000000000100000000, "It's an account for users whose primary account is in another domain. This account provides user access to this domain, but not to any domain that trusts this domain. It's sometimes referred to as a local user account.")
    NORMAL_ACCOUNT                 = (0b00000000000000000000001000000000, "It's a default account type that represents a typical user.")
    RESERVED_B10                   = (0b00000000000000000000010000000000, "Reserved bit 10")
    INTERDOMAIN_TRUST_ACCOUNT      = (0b00000000000000000000100000000000, "It's a permit to trust an account for a system domain that trusts other domains.")
    WORKSTATION_TRUST_ACCOUNT      = (0b00000000000000000001000000000000, "It's a computer account for a computer that is running Microsoft Windows NT 4.0 Workstation, Microsoft Windows NT 4.0 Server, Microsoft Windows 2000 Professional, or Windows 2000 Server and is a member of this domain.")
    SERVER_TRUST_ACCOUNT           = (0b00000000000000000010000000000000, "It's a computer account for a domain controller that is a member of this domain.")
    RESERVED_B14                   = (0b00000000000000000100000000000000, "Reserved bit 14")
    RESERVED_B15                   = (0b00000000000000001000000000000000, "Reserved bit 15")
    DONT_EXPIRE_PASSWORD           = (0b00000000000000010000000000000000, "Represents the password, which should never expire on the account.")
    MNS_LOGON_ACCOUNT              = (0b00000000000000100000000000000000, "It's an MNS logon account.")
    SMARTCARD_REQUIRED             = (0b00000000000001000000000000000000, "When this flag is set, it forces the user to log on by using a smart card.")
    TRUSTED_FOR_DELEGATION         = (0b00000000000010000000000000000000, "When this flag is set, the service account (the user or computer account) under which a service runs is trusted for Kerberos delegation. Any such service can impersonate a client requesting the service. To enable a service for Kerberos delegation, you must set this flag on the userAccountControl property of the service account.")
    NOT_DELEGATED                  = (0b00000000000100000000000000000000, "When this flag is set, the security context of the user isn't delegated to a service even if the service account is set as trusted for Kerberos delegation.")
    USE_DES_KEY_ONLY               = (0b00000000001000000000000000000000, "(Windows 2000/Windows Server 2003) Restrict this principal to use only Data Encryption Standard (DES) encryption types for keys.")
    DONT_REQ_PREAUTH               = (0b00000000010000000000000000000000, "(Windows 2000/Windows Server 2003) This account doesn't require Kerberos pre-authentication for logging on.")
    PASSWORD_EXPIRED               = (0b00000000100000000000000000000000, "(Windows 2000/Windows Server 2003) The user's password has expired.")
    TRUSTED_TO_AUTH_FOR_DELEGATION = (0b00000001000000000000000000000000, "(Windows 2000/Windows Server 2003) The account is enabled for delegation. It's a security-sensitive setting. Accounts that have this option enabled should be tightly controlled. This setting lets a service that runs under the account assume a client's identity and authenticate as that user to other remote servers on the network.")
    RESERVED_B25                   = (0b00000010000000000000000000000000, "Reserved bit 25")
    PARTIAL_SECRETS_ACCOUNT        = (0b00000100000000000000000000000000, "(Windows Server 2008/Windows Server 2008 R2) The account is a read-only domain controller (RODC). It's a security-sensitive setting. Removing this setting from an RODC compromises security on that server.")
    RESERVED_B27                   = (0b00001000000000000000000000000000, "Reserved bit 27")
    RESERVED_B28                   = (0b00010000000000000000000000000000, "Reserved bit 28")
    RESERVED_B29                   = (0b00100000000000000000000000000000, "Reserved bit 29")
    RESERVED_B30                   = (0b01000000000000000000000000000000, "Reserved bit 30")
    RESERVED_B31                   = (0b10000000000000000000000000000000, "Reserved bit 31")

class sAMAccountType(Enum):
    # https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-samr/e742be45-665d-4576-b872-0bc99d1e1fbe
    SAM_DOMAIN_OBJECT = (0x00000000, "Represents a domain object.")
    SAM_GROUP_OBJECT = (0x10000000, "Represents a group object.")
    SAM_NON_SECURITY_GROUP_OBJECT = (0x10000001, "Represents a group object that is not used for authorization context generation.")
    SAM_ALIAS_OBJECT = (0x20000000, "Represents an alias object.")
    SAM_NON_SECURITY_ALIAS_OBJECT = (0x20000001, "Represents an alias object that is not used for authorization context generation.")
    SAM_USER_OBJECT = (0x30000000, "Represents a user object.")
    SAM_MACHINE_ACCOUNT = (0x30000001, "Represents a computer object.")
    SAM_TRUST_ACCOUNT = (0x30000002, "Represents a user object that is used for domain trusts.")
    SAM_APP_BASIC_GROUP = (0x40000000, "Represents an application-defined group.")
    SAM_APP_QUERY_GROUP = (0x40000001, "Represents an application-defined group whose members are determined by the results of a query.")

## Main

def parseArgs():
    parser = argparse.ArgumentParser(description="Description message")
    # todo, list of attributes in argument
    parser.add_argument("attribute", default=None, help="attribute")
    parser.add_argument("value", default=None, help="value")

    parser.add_argument("-b", "--bits", default=False, required=False, action='store_true', help="Show bits masks.")
    parser.add_argument("-v", "--verbose", default=False, required=False, action='store_true', help="Verbose mode.")
    parser.add_argument("--colors", default=False, required=False, action='store_true', help="Print with colors.")
    return parser.parse_args()


if __name__ == '__main__':
    options = parseArgs()

    if options.attribute.lower() == "userAccountControl".lower():
        bits = 32
        options.value = int(options.value)
        if options.bits == True:
            print("[>] %-30s : %s" % ("userAccountControl value", bin(options.value)[2:].rjust(bits, '0').replace('0', '.')))
        else:
            print("[>] %-30s : %s" % ("userAccountControl value", hex(options.value)))
        for flag in sorted(list(userAccountControl), key=lambda x: x.value, reverse=True):
            if flag.value[0] & options.value == flag.value[0]:
                if options.bits == True:
                    if options.colors:
                        print("[\x1b[92m█\x1b[0m] %-30s : %s" % (
                            str(flag).split('.', 1)[1],
                            bin(flag.value[0])[2:].rjust(bits, '0').replace('0', '.').replace("1", "\x1b[1;92m1\x1b[0m")
                        ))
                    else:
                        print("  | %-30s : %s" % (
                            str(flag).split('.', 1)[1],
                            bin(flag.value[0])[2:].rjust(bits, '0').replace('0', '.')
                        ))
                else:
                    if options.colors:
                        print("[\x1b[92m█\x1b[0m] %-30s : %s" % (str(flag).split('.', 1)[1], flag.value[1]))
                    else:
                        print("  | %-30s : %s" % (str(flag).split('.', 1)[1], flag.value[1]))
            else:
                if options.verbose == True:
                    if options.bits == True:
                        if options.colors:
                            print("[\x1b[91m█\x1b[0m] %-30s : %s" % (
                                str(flag).split('.', 1)[1],
                                bin(flag.value[0])[2:].rjust(bits, '0').replace('0', '.').replace("1", "\x1b[91m1\x1b[0m")
                            ))
                        else:
                            print("[>] %-30s : %s" % (
                                str(flag).split('.', 1)[1],
                                bin(flag.value[0])[2:].rjust(bits, '0').replace('0', '.')
                            ))
                    else:
                        if options.colors:
                            print("[\x1b[91m█\x1b[0m] %-30s : %s" % (str(flag).split('.', 1)[1], flag.value[1]))
                        else:
                            print("[>] %-30s : %s" % (str(flag).split('.', 1)[1], flag.value[1]))

    elif options.attribute.lower() == "sAMAccountType".lower():
        bits = 32
        options.value = int(options.value)
        if options.bits == True:
            print("[>] %-25s : %s" % ("sAMAccountType value", bin(options.value)[2:].rjust(bits, '0').replace('0', '.')))
        else:
            print("[>] %-25s : %s" % ("sAMAccountType value", hex(options.value)))
        try:
            tmpvalue = None
            for v in list(sAMAccountType):
                if v.value[0] == options.value:
                    tmpvalue = v
            #
            if tmpvalue is None:
                raise ValueError("%s is not a valid sAMAccountType" % hex(options.value))
            #
            if (tmpvalue in list(sAMAccountType)):
                if options.bits == True:
                    if options.colors:
                        print("[\x1b[92m█\x1b[0m] %-25s : %s" % (
                            str(tmpvalue).split('.', 1)[1],
                            bin(tmpvalue.value[0])[2:].rjust(bits, '0').replace('0', '.')
                        ))
                    else:
                        print("  | %-25s : %s" % (
                            str(tmpvalue).split('.', 1)[1],
                            bin(tmpvalue.value[0])[2:].rjust(bits, '0').replace('0', '.')
                        ))
                else:
                    if options.colors:
                        print("[\x1b[92m█\x1b[0m] %-25s : %s" % (str(tmpvalue).split('.', 1)[1], tmpvalue.value[1]))
                    else:
                        print("  | %-25s : %s" % (str(tmpvalue).split('.', 1)[1], tmpvalue.value[1]))
        except ValueError as e:
            print("[!] %s is not a valid sAMAccountType" % hex(options.value))
            pass

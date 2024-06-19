# -------------------------------------------------------------------------------- #

# ----------------------------------------
#   Legend:
#   0 - None
#   1 - Flashlight ON/OFF
#   2 - Power Select
#   3 - Monitor
#   4 - Scan ON/OFF
#   5 - VOX ON/OFF
#   6 - Alarm ON/OFF
#   7 - FM Radio
#   8 - Transmitting 1750
# ----------------------------------------

KeyPress = {
    "Key1ShortPress":   3,
    "Key1LongPress":    7,
    "Key2ShortPress":   1,
    "Key2LongPress":    1
}

# -------------------------------------------------------------------------------- #

Common = {
    "MaxTalkTime":          2,
    "BackLight":            5,
    "ChanDisplayFlag":      0,
    "PowerSave":            4,
    "TailToneFlag":         1,
    "VFOFlag":              1,
    "VoxLevel":             5,
    "FastCallChannel":      0,
    "MicSensitiveLevel":    3,
    "DoubleWaitFlag":       1,
    "SQLLevel":             2,
    "BandDiffRxTx":         0,
    "KeyToneFlag":          0,
    "Language":             1,
    "BeepFlag":             0,
    "AutoKeyLock":          0,
    "ScanRestore":          1,
    "WelcomeDisplay":       1,
    "AlarmType":            1,
    "OverTone":             0,
    "ToneClearFlag":        0,
    "LogoStr1":             "WELCOME",
    "LogoStr2":             "",
    "AllowKill":            "False",
    "NOAAScanFlag":         1,
    "AccessPwd":            "/DGzTcf8uU4="  # no password
}

# -------------------------------------------------------------------------------- #

DTMF = {
    "LocalNo":          102,
    "KillNo":           77777,
    "ActiveNo":         88888,
    "SeparatorNo":      "*",
    "GroupNo":          "#",
    "ResetTimeLen":     5,
    "DecodeRsp":        0,
    "UpCode":           123,
    "DownCode":         456,
    "SideTone":         1,
    "BeforehandTime":   300,
    "FirstCodeTime":    100,
    "StarCodeTime":     100,
    "CodeTime":         100,
    "CodeInterval":     100
}

# -------------------------------------------------------------------------------- #

Contacts = {
    "Contact": [
        {"DTMFName": "CALL1", "DTMFCode": 101},
        {"DTMFName": "CALL2", "DTMFCode": 102},
        {"DTMFName": "CALL3", "DTMFCode": 103},
        {"DTMFName": "CALL4", "DTMFCode": 104},
        {"DTMFName": "CALL5", "DTMFCode": 105}
    ]
}

# -------------------------------------------------------------------------------- #

Channels_default = {
    "Name": "CH001",
    "chanIndex": 0,
    "BandWidth": 0,
    "TxFreq": "144,025",
    "RxFreq": "144,025",
    "TxPowerLevel": 0,
    "AnaTxCTCFlag": 0,
    "AnaRxCTCFlag": 0,
    "AnaTxCTCIndex": 0,
    "AnaRxCTCIndex": 0,
    "FreqStep": 1,
    "FreqReverseFlag": 0,
    "EncryptFlag": 0,
    "BusyNoTx": 1,
    "PTTIdFlag": 0,
    "DTMFDecode": 0,
    "AMChanFlag": 0
}

# -------------------------------------------------------------------------------- #

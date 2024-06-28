Sub Shell(cmd)
    Dim objShell
    Set ObjShell = WScript.CreateObject("WScript.Shell")
    objShell.Run(cmd)
    Set ObjShell = Nothing
End Sub

Public Function Kill_Executable(Exe_Name)
    On Error Resume Next
    strComputer = "."
    Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\cimv2")
    Set colProcessList = objWMIService.ExecQuery ("Select * from Win32_Process Where Name = '"&Exe_Name&"'")
    For Each objProcess In colProcessList
        objProcess.Terminate()
    Next
    Set colProcessList = Nothing
    Set objWMIService = Nothing
    On Error Goto 0
End Function

Set wsc = CreateObject("WScript.Shell")
Do
    WScript.Sleep (300*100)
    wsc.SendKeys "%({NUMLOCK})"
    ''              Shell "cmd"
    ''              Kill_Executable "cmd.exe"
Loop
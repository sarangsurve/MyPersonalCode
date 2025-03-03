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

Hello Manish,

Please accept this letter as my formal resignation from the position of Senior Analyst in Data Engineering, Management, and Governance at Accenture. While I am aware of the 90-day notice period, I would like to request an early release with the option of a buyout to expedite the transition. 

I have enjoyed serving at Accenture over the past 25 months, and I appreciate the opportunities provided to me. It has been an enriching and transformative experience, and I am thankful to my colleagues and the leadership for their support.

During my notice period, I will ensure a smooth handover of all responsibilities and assist with any necessary transitions during my notice period.

Thank you granting me such an opportunity to work at Accenture and I hope my request will be considered. I look forward to your guidance on the next steps.

Sincerely,
Sarang Surve

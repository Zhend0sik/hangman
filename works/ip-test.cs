IPHostEntry host1 = Dns.GetHostEntry("www.microsoft.com");
Console.WriteLine(host1.HostName);
foreach (IPAddress ip in host1.AddressList)
    Console.WriteLine(ip.ToString());

Console.WriteLine();

IPHostEntry host2 = Dns.GetHostEntry("google.com");
Console.WriteLine(host2.HostName);
foreach (IPAddress ip in host2.AddressList)
    Console.WriteLine(ip.ToString());

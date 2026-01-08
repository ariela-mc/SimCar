// See https://aka.ms/new-console-template for more information
using System.Threading.Tasks;

string appName = "Simulated Car";
string appVersion = "1.0.0";
string appAuthor = "Ariela Mcclame";

//change text color
Console.ForegroundColor = ConsoleColor.Green;
// write out app info
Console.WriteLine("{0}: Version {1} by {2}", appName, appVersion, appAuthor);

//clear text color
Console.ResetColor();

int battery = 100;
bool charging = false;

while (true)
{
    if (!charging)
    // go down slowly if battery not charging
    {
        if (battery > 0)
        {
            battery--;
        } 
    } else
    // charge quickly if charging
    {
        if (battery < 100)
        {
            battery += 2;
        } 
    }
    // Wait for 2000 milliseconds (2 seconds) asynchronously
    await Task.Delay(1000);
    Console.WriteLine("Battery: {0}", battery);
    Console.WriteLine("Charging: {0}", charging);
}

using System;

namespace guessTheNumber {
    class Program {
        static void Main(string[] args) {  
            string appName = "GuessMyNumber";
            string version = "v0.0.1";
            string author = "Iqbal";

            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("{0} {1} By {2}", appName, version, author);
            Console.ResetColor();

            System.Threading.Thread.Sleep(1000);
            Console.Clear();

            Console.WriteLine("Hi");
            System.Threading.Thread.Sleep(1000);
            Console.WriteLine("What's your Name?");
       
            string userName = Console.ReadLine();
            StartGame:
            Console.Clear();
            System.Threading.Thread.Sleep(1000);
            Console.WriteLine("Okay {0}, Let's do it.\n" +
                            "I have a number(1~100) in my mind.\n" +
                            "Can you guess it?", userName);

            Random rndm = new Random();
            int thoughtNumber = rndm.Next(1, 100);
           
            while (true) {
                string inp = Console.ReadLine();
                int guessedNumber;
                try {
                    guessedNumber = int.Parse(inp);
                    if (guessedNumber < 0 || guessedNumber > 100) throw new Exception("Try a number 1~100");
                }
                catch(Exception e){
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("[ERROR] " + e.Message);
                    Console.ResetColor();
                    continue;
                }

                if(guessedNumber == thoughtNumber) {
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine("You are CORRECT!");
                    Console.ResetColor();
                    
                    Console.WriteLine("Do you want to play again? [Y/N]");
                    GamePlan:
                    string cmd = Console.ReadLine();
                    if (cmd == "y" || cmd == "Y") goto StartGame;
                    else if (cmd == "n" || cmd == "N") goto EndGame;
                    else {
                        Console.WriteLine("[Y/n] -_-");
                        goto GamePlan;
                    }
                }
                else if(guessedNumber > thoughtNumber) {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("[HINT] Try a smaller number!");
                    Console.ResetColor();
                }
                else {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("[HINT] Try a bigger number!");
                    Console.ResetColor();
                }
            }

        EndGame:
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.Clear();
            Console.WriteLine("Thanks for playing.");
            System.Threading.Thread.Sleep(1000);

            Console.Clear();
            Console.WriteLine("Bye!");
            System.Threading.Thread.Sleep(1000);
        }
    }
}

import java.util.Scanner;
import java.io.*;

//Program is a more complex BTU calculator depending on the room which will have the greastest amount of Btus needed or the least amout needed.

    
   public class complex_BTU
   
{
    public static void main(String[] args) throws IOException 
       {
       Scanner keyboard = new Scanner(System.in);
            
//Opening the file
      File file = new File("Rooms.txt");
      Scanner inputFile= new Scanner(file);
      
//Reading the next room
      // Title of the program
   System.out.println("Air Conditioning Window Unit Cooling Capacity");
   
//Displaying the names
   while (inputFile.hasNext())
   { 
   
   String line = inputFile.nextLine();
   System.out.println(line);
    
    
// Inputting the data as from project 1
       double length, width;
       double area;
       double options;
 
//Get length and width
       System.out.print("Enter length in feet: ");
       length = keyboard.nextDouble();
       System.out.print("Enter width in feet: ");
       width = keyboard.nextDouble();
 
 double roomOptions;
       
       System.out.print("How much shade does the room receive?:\n ");
       
       System.out.print( "\t1. Abundant\n\t2. Moderate\n\t3. Little\n");
     
       System.out.print("Please enter from the options above: ");
       roomOptions = keyboard.nextDouble();
  options = roomOptions;
       if (roomOptions == 3)  
         System.out.println("Amount of shade: Little");
       else if (roomOptions == 2)
       System.out.println("Amount of shade: Moderate");
         else 
            System.out.println("Amount of shade: Abundant");
        
         area = length * width;
       System.out.println("Room area(in sqaure feet):" + area );

double room, btu;

      if (area < 250)
         btu = 5500;
      else if (area < 500)
         btu = 10000;  
      else if (area < 1000)
         btu = 17500;
      else
      btu = 24000; 
     area = length * width;
         
         room = btu;
         
room = btu;

   if (roomOptions == 3)
      room = btu * 1.15;
   else if (roomOptions == 2)
      room = btu;
   else 
      room = btu * .90;
      System.out.print("BTU's Per Hour Needed:" + room);

 }
 
           
 inputFile.close();        

      
      
       }
}       
      



   
 


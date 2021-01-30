/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package project3;

import java.util.Scanner;

/**
 *
 * @author micha
 */
public class Project3 {

    /** using the equation from the previous method the user is able to type a number
     * between 1 -10 and get the partition of that.
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        //Using scanner class to allow iuser to input a number
        System.out.print("What is the number?: ");
        int x = scan.nextInt();
        //not allowing th enuber to go below 1 or above 10
        if (x <= 0 || x >= 11) {
            System.out.println("Try a number between 1 - 10");
        } else {
            System.out.println(part(x));
        }

        System.out.println("Thank you for letting me hand it in late :)");

    }

    /**
     *This method is making the equation for the project 
     * @param num
     * @return
     */
    public static int part(int num) {

        if (num <= 1) {
            return num;

        } else {
            return part(num - 1) + part(num / 2);
        }

    }
}

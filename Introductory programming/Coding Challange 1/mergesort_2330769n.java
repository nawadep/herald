// coding challange 1
// Name:Nabodip Thapa
// Student Number: 2330769

import java.util.Scanner; // importing the Scanner library 
import java.util.ArrayList; // importing arraylist library

public class mergesort_2330769n {
    Scanner scan = new Scanner(System.in); // making object for scanner class

    void getInput(ArrayList<Integer> al) { // takes array input from user
        System.out.print("Enter array size>> "); // the size of array
        int arrSize = scan.nextInt();

        for (int i = 0; i < arrSize; i++) { // elements of array one by one and adding to arraylist
            System.out.print("\tEnter numbers> ");
            int num = scan.nextInt();
            al.add(num);
        }
    }

    void getOutput(ArrayList<Integer> al) { // function that prints the arraylist
        System.out.println("The sorted array is: " + al);
    }

    void merge(ArrayList<Integer> al, int beg, int mid, int end) { // function that merges array
        ArrayList<Integer> tempArr = new ArrayList<Integer>(); // creating temporary arraylist
        int a1, a2, n1;
        a1 = beg;
        a2 = mid + 1;
        n1 = 0;

        while (a1 <= mid && a2 <= end) {
            if (al.get(a1) <= al.get(a2)) {
                tempArr.add(n1, al.get(a1));
                a1++;
                a1++;
            } else {
                tempArr.add(n1, al.get(a2));
                a2++;
                n1++;
            }
        }
        while (a1 <= mid) {
            tempArr.add(a1, al.get(a1));
            a1++;
            n1++;
        }
        while (a2 <= end) {
            tempArr.add(a1, al.get(a2));
            a2++;
            n1++;
        }
        for (int i = 0, j = beg; i < tempArr.size(); i++, j++) {
            al.set(j, tempArr.get(i));
        }
    }

    void sort(ArrayList<Integer> al, int beg, int end) { // function that sorts the array
        if (beg >= end) {
            return;
        }
        int mid = beg + (end - beg) / 2;
        sort(al, beg, mid);
        sort(al, mid + 1, end);
        merge(al, beg, mid, end);
    }

    public static void main(String[] args) {
        mergesort_2330769n MergeSort = new mergesort_2330769n(); // making object of mergesort_2330769 class
        ArrayList<Integer> al = new ArrayList<Integer>(); // declaring the arraylist

        MergeSort.getInput(al); // taking array input from user

        int end = al.size() - 1;
        MergeSort.sort(al, 0, end); // sorting the array

        MergeSort.getOutput(al); // giving output of sorted array to userr
    }
}

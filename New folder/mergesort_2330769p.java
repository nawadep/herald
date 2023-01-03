//Name: NabodipThapa
import java.util.*;
//creating class MergeSort_2330769
public class mergesort_2330769p{
    //creating method getInput
    public static void getInput(ArrayList<Integer> al) {
        //creating object input for scanner
        Scanner input = new Scanner(System.in);
        //asking user the length of an array
        System.out.println("Enter the length of array: ");
        int size = input.nextInt();
        for (int i = 0; i < size; i++) {
            System.out.println("Enter the number for index " + i);
            al.add(input.nextInt());
        }
        System.out.println("Unsorted array: ");
        System.out.println(al);
    }
    //creating method getOutput
    public static void getOutput(ArrayList<Integer> al) {
        System.out.println("Sorted Array: ");
        System.out.print("[");
        for (int i = 0; i < al.size(); i++) {
            if (i == al.size() - 1) {
                System.out.print(al.get(i));
            } else {
                System.out.print(al.get(i) + ", ");
            }
        }
        System.out.print("]");
    }
    //creating method merge
    public static void merge(ArrayList<Integer> al, int beg, int mid, int end) {
        int beginning = beg;
        int midIndex = mid + 1;
        int ending = end;

        while (beg <= midIndex && midIndex <= end) {
            if (al.get(beg) > (al.get(midIndex))){
                al.add(beg, al.remove(midIndex));
                beg++;
                midIndex++;
            } else if (Objects.equals(al.get(beg), al.get(midIndex))) {
                al.add(beg , al.remove(midIndex));
                beg++;
                midIndex++;
            } else {
                beg++;
            }
        }
    }
    //creating method sort
    public static void sort(ArrayList<Integer> al, int begin, int end) {
        if(begin<end) {
            int mid = (begin + end) / 2;
            sort(al, begin, mid);
            sort(al,mid+1, end);
            merge(al, begin, mid, end);
        }
    }
    //main function
    public static void main(String[] args) {
        //creating object for this class
        mergesort_2330769p object = new mergesort_2330769p();
        ArrayList<Integer> al = new ArrayList<>();
        //calling the methods
        object.getInput(al);
        object.sort(al, 0, al.size()-1);
        object.getOutput(al);
    }
}
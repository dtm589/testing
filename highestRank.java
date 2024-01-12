'''
write a class StudentRank with two member varaibles names studesntsm a string array, and ranks, an integer array. Add a method, highestRank, that returns the highest-ranked student. Also write a lowestRank method which provies the name of the lowest ranked student. The primary constructor should accept the student and ranks array. 
'''

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;


class StudentRank{
    private String[] students;
    private int[] ranks;
    
    public StudentRank(String[] students, int[] ranks) {
        this.students = students;
        this.ranks = ranks;
    }
    
    public String highestRank() {
        if (students == null || ranks == null || students.length == 0 || ranks.length == 0) {
            return "No students or ranks provided";
        }
        
        int maxRankIndex = indexOfMaxRank();
        return students[maxRankIndex];
    }
    
    public String lowestRank() {
        if (students == null || ranks == null || students.length == 0 || ranks.length == 0) {
            return "No students or ranks provided";
        }
        
        int minRankIndex = indexOfMinRank();
        return students[minRankIndex];
    }
    
    private int indexOfMaxRank() {
        int maxRank = ranks[0];
        int maxRankIndex = 0;
        
        for (int i = 1; i < ranks.length; i++) {
            if (ranks[i] > maxRank) {
                maxRank = ranks[i];
                maxRankIndex = i;
            }
        }
        
        return maxRankIndex;
    }
    
    private int indexOfMinRank() {
        int minRank = ranks[0];
        int minRankIndex = 0;
        
        for (int i = 1; i < ranks.length; i++) {
            if(ranks[i] < minRank) {
                minRank = ranks[i];
                minRankIndex = i;
            }
        }
        return minRankIndex;
    }
}
public class Solution {
    public static void main(String[] args) throws IOException {
        //reader and writer
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));             
        BufferedWriter bufferedWriter = new BufferedWriter(new 
                FileWriter(System.getenv("OUTPUT_PATH")));
        
        //read input
        String[] students = bufferedReader.readLine().replaceAll("\\s+$", "").split(",");
        String[] ranksStr = bufferedReader.readLine().replaceAll("\\s+$", "").split(",");
        
        int[] ranks = new int[ranksStr.length];
        for(int i=0; i< ranksStr.length; i++){
            ranks[i] = Integer.valueOf(ranksStr[i]).intValue();
        }

        StudentRank sr = new StudentRank(students,ranks);
        
        bufferedWriter.write(sr.highestRank() + "," + sr.lowestRank());
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
     }
}

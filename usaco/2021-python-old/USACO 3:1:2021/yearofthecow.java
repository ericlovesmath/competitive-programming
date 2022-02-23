/*
 ID: dazzlethelightwing
 LANG: JAVA
 PROG: year
*/

import java.io.*;
import java.util.*;

class yearofthecow {
  public static void main (String [] args) throws IOException {
    
    HashMap<String, Integer> person = new HashMap<>();
    person.put("Bessie", 0);

    HashMap<String, String> person_year = new HashMap<>();
    person_year.put("Bessie", "Ox");

    HashMap<String, Integer> zodiac = new HashMap<>();
    zodiac.put("Ox", 0);
    zodiac.put("Tiger", 1);
    zodiac.put("Rabbit", 2);
    zodiac.put("Dragon", 3);
    zodiac.put("Snake", 4);
    zodiac.put("Horse", 5);
    zodiac.put("Goat", 6);
    zodiac.put("Monkey", 7);
    zodiac.put("Rooster", 8);
    zodiac.put("Dog", 9);
    zodiac.put("Pig", 10);
    zodiac.put("Rat", 11);

    BufferedReader f = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer string_token = new StringTokenizer(f.readLine());
    int num_of_statements = Integer.parseInt(string_token.nextToken());
    for (int i = 0; i < num_of_statements; i++)
    {
        string_token = new StringTokenizer(f.readLine());
        String man_1 = string_token.nextToken();
        string_token.nextToken();
        string_token.nextToken();
        String PrevNext = string_token.nextToken();
        String year = string_token.nextToken();
        string_token.nextToken();
        string_token.nextToken();
        String man_2 = string_token.nextToken();

        if (!person.containsKey(man_1))
        {
            person.put(man_1, 0);
        }
        person_year.put(man_1, year);

        if (PrevNext.equals("previous"))
        {
            int diff = 12 - zodiac.get(year) + zodiac.get(person_year.get(man_2)) + person.get(man_2);
            person.put(man_1, diff);
        }
        else 
        {
            int diff = 12 + zodiac.get(year) - zodiac.get(person_year.get(man_2)) - person.get(man_2);
            person.put(man_1, diff);
        }
    }
    System.out.println(Math.abs(person.get("Elsie")));
  }
}
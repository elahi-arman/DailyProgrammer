import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Challenge_223{

	public static void main(String[] args){
		System.out.println(easy("ceramic", "c", 0));
		System.out.println(easy("onion", "o", 0));
		System.out.println(easy("alfalfa", "a", 0));
	}

	//Eel of Fortune -- Find problem words in a string
	public static boolean intermediate(String eel, String offensive){
		if ((eel.length() == 1 && eel.substring(eel.length()).equals(offensive)) || offensive.length() == 0)
			return true;
		else if (eel.indexOf(offensive.charAt(0)) == -1)
			return false;
		else
			return intermediate(eel.substring(eel.indexOf(offensive.charAt(0))), offensive.substring(1));
	}

	public static void testIntermediate(String offensive){
		ArrayList<String> word_list = new ArrayList<String>();
		word_list = readFile("./enable1.txt");
		for (String s: word_list){
			if (intermediate(s, offensive))
				System.out.println(s);
		}
	}

	public static ArrayList<String> readFile(String path){
		ArrayList<String> dictionary = new ArrayList<String>();

		try (BufferedReader  br = new BufferedReader(new FileReader(path))){
			String brCurrentLine;
			//first we'll write this explicitly so that it's easier to debug
			while((brCurrentLine = br.readLine()) != null){
				dictionary.add(brCurrentLine);
			}
		}	catch (IOException e){
			e.printStackTrace();
		}

		return dictionary;
	}
}

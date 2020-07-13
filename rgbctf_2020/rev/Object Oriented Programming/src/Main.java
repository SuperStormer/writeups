//I heard Java 11 is good, let's use that
import java.io.*;
import java.math.*;
import java.util.*;
import java.lang.reflect.*;//think of this as #include <stdio.h>, basically every program needs it for IO

public class Main {
	//it's always good practice to declare constants for unclear magic values
	public static final int ZERO = BigInteger.valueOf(0).intValue();//BigInteger for precision
	public static final int ONE = BigInteger.valueOf(1).intValue();
	public static final int TWO = BigInteger.valueOf(2).intValue();
	public static final int THREE = BigInteger.valueOf(3).intValue();
	public static final int FOUR = BigInteger.valueOf(4).intValue();
	public static final int SEVEN = BigInteger.valueOf(7).intValue();
	public static final int SIXTEEN = BigInteger.valueOf(16).intValue();
	
	public static void main(String[] args) throws Exception { //running Java is dangerous, that's why everything throws an Exception
		InputStream standardInputStream = new StandardInputStreamInstantiator().getStandardInputStreamFactory().getStandardInputStream();
		//i'm going to take a shortcut here, behold the power of java libraries - so many lines saved!
		Scanner scanner = Scanner.class.getConstructor(standardInputStream.getClass().getSuperclass().getSuperclass()).newInstance(standardInputStream);
		
		PrintStream outputPrintStream = new OutputPrintStreamInstantiator().getOutputPrintStreamFactory().getOutputPrintStream();
		Method printLineMethod = getPrintLineMethodForOutputPrintStream(outputPrintStream);
		invokePrintLineMethodForOutputPrintStream(outputPrintStream, printLineMethod, "IO is online.");
		//IO Setup
		
		String userInput = getUserInputMethodFromScannerAndInvokeAndReturnOutput(scanner);
		if (userInput.length() != SIXTEEN)
			System.exit(0);
		
		
		if (executeCodeThatDoesSomethingThatYouProbablyNeedToFigureOut(userInput).equals(scanner.getClass().getPackageName().replace(".", ""))) {
			invokePrintLineMethodForOutputPrintStream(outputPrintStream, printLineMethod, "Nice. Flag: rgbCTF{" + userInput + "}");
		} else {
			invokePrintLineMethodForOutputPrintStream(outputPrintStream, printLineMethod, "Try again.");
		}
	}
	
	public static String executeCodeThatDoesSomethingThatYouProbablyNeedToFigureOut(String stringToExecuteAforementionedCodeOn) throws Exception {
		String encryptedString = reallyBasicQuoteUnquoteEncryptionFunctionThatWillOnlyTakeTimeToFigureOutIfYouKeepReadingTheseRidiculouslyLongMethodNames(stringToExecuteAforementionedCodeOn);
		String returnValueOfThisFunction = new String();
		String[] chunksOfEncryptedStringOfLengthFour = splitStringIntoChunksOfLength(encryptedString, FOUR);
		for (String chunkOfEncryptedStringOfLengthFour : chunksOfEncryptedStringOfLengthFour) {
			String[] chunksOfChunkOfEncryptedStringOfLengthFourOfLengthTwo = splitStringIntoChunksOfLength(chunkOfEncryptedStringOfLengthFour, TWO);
			String firstChunkOfChunkOfEncryptedStringOfLengthFourOfLengthTwo = chunksOfChunkOfEncryptedStringOfLengthFourOfLengthTwo[0];
			String secondChunkOfChunkOfEncryptedStringOfLengthFourOfLengthTwo = chunksOfChunkOfEncryptedStringOfLengthFourOfLengthTwo[1];
			Class<?> classAndExtraCharactersSoItsNotAKeyword = Class.forName(firstChunkOfChunkOfEncryptedStringOfLengthFourOfLengthTwo);
			Object object = classAndExtraCharactersSoItsNotAKeyword.getConstructors()[ZERO].newInstance();
			for (int loopArbitraryCounterIterator = 0; loopArbitraryCounterIterator < THREE; loopArbitraryCounterIterator++) {
				Method method = classAndExtraCharactersSoItsNotAKeyword.getMethod(secondChunkOfChunkOfEncryptedStringOfLengthFourOfLengthTwo);
				secondChunkOfChunkOfEncryptedStringOfLengthFourOfLengthTwo = (String)method.invoke(object);
			}
			returnValueOfThisFunction = new String(returnValueOfThisFunction + secondChunkOfChunkOfEncryptedStringOfLengthFourOfLengthTwo);
		}
		return returnValueOfThisFunction;
	}
	
	protected static char secureEncryptionKey; //it's protected, how you gonna crack it now?
	
	public static String reallyBasicQuoteUnquoteEncryptionFunctionThatWillOnlyTakeTimeToFigureOutIfYouKeepReadingTheseRidiculouslyLongMethodNames(String stringToQuoteUnquoteEncrypt) throws Exception {
		secureEncryptionKey = new EncryptionKeyInstantiator().getEncryptionKeyFactory().getEncryptionKey();
		Integer[] encryptedArrayToBeCalledByStringConstructor = new Integer[stringToQuoteUnquoteEncrypt.length()];
		for (int loopIndexIterator = ZERO; loopIndexIterator < stringToQuoteUnquoteEncrypt.length(); loopIndexIterator++) {
			encryptedArrayToBeCalledByStringConstructor[loopIndexIterator] = stringToQuoteUnquoteEncrypt.charAt(loopIndexIterator)^secureEncryptionKey;
		}
		
		return Arrays.toString(Arrays.asList(encryptedArrayToBeCalledByStringConstructor).stream().map((currentIntegerToBeMapped) -> (char)(currentIntegerToBeMapped.intValue())).toArray(Character[]::new)).replaceAll(", ", "").substring(1, stringToQuoteUnquoteEncrypt.length() + ONE);
	}
	
	public static String[] splitStringIntoChunksOfLength(String stringToSplit, int lengthOfChunk) {
		String[] returnValueOfThisFunction = new String[stringToSplit.length() / lengthOfChunk];
		for (int loopChunkNumberIterator = ZERO; loopChunkNumberIterator < stringToSplit.length() / lengthOfChunk; loopChunkNumberIterator++) {
			returnValueOfThisFunction[loopChunkNumberIterator] = stringToSplit.substring(loopChunkNumberIterator * lengthOfChunk, loopChunkNumberIterator * lengthOfChunk + lengthOfChunk);
		}
		return returnValueOfThisFunction;
	}
	
	private static class EncryptionKeyInstantiator {
		public EncryptionKeyFactory getEncryptionKeyFactory() {
			return new EncryptionKeyFactory();
		}
		
		private class EncryptionKeyFactory {
			public char getEncryptionKey() {
				return (char)(this.getClass().getCanonicalName().charAt(SEVEN) - this.getClass().getCanonicalName().charAt(ONE));
			}																																																																																		
		}
	}
	
	//IO Setup Setup
	
	public static String getUserInputMethodFromScannerAndInvokeAndReturnOutput(Scanner scanner) throws Exception {
		return (String)scanner.getClass().getMethod("nextLine").invoke(scanner);
	}
	
	public static void invokePrintLineMethodForOutputPrintStream(PrintStream outputPrintStream, Method printLineMethodToInvoke, String stringToBePrintedByPrintLineMethod) throws Exception {
		printLineMethodToInvoke.invoke(outputPrintStream, stringToBePrintedByPrintLineMethod);
	}
	
	public static Method getPrintLineMethodForOutputPrintStream(PrintStream outputPrintStream) throws Exception{
		return outputPrintStream.getClass().getMethod("println", String.class);
	}
	
	private static class OutputPrintStreamInstantiator {
		public OutputPrintStreamFactory getOutputPrintStreamFactory() throws Exception{
			return new OutputPrintStreamFactory();
		}
		
		private class OutputPrintStreamFactory {
			public PrintStream getOutputPrintStream() throws Exception {
				return (PrintStream)System.class.getDeclaredField("out").get(null);
			}
		}
	}
	
	private static class StandardInputStreamInstantiator {
		public StandardInputStreamFactory getStandardInputStreamFactory() throws Exception {
			return new StandardInputStreamFactory();
		}
		
		private class StandardInputStreamFactory {
			public InputStream getStandardInputStream() throws Exception {
				return (InputStream)System.class.getDeclaredField("in").get(null);
			}
		}
	}
}

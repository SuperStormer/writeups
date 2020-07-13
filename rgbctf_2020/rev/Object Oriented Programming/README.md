# Object Oriented Programming

Source: [src/](./src)

Reading the code of questionable quality, we see 2 functions that perform the encryption:

```java
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
```

The second function is just xor with `secureEncryptionKey` which we find is 2. The first function iterates through each chunk of 4 chars and uses the other classes as a lookup table. We can reverse this logic.

Final Exploit: [oop.py](./oop.py)

Flag: rgbCTF{enterprisecodeee}

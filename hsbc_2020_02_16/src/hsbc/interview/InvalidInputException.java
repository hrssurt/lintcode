package hsbc.interview;

public class InvalidInputException extends Exception{
	public InvalidInputException(String errorMessage) {
		super(errorMessage);
	}
}
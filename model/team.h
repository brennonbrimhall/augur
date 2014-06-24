struct Team {
	private:
		int teamNumber;
		int firstSort, secondSort, thirdSort, fourthSort, fifthSort;
	public:
		int getFirstSort();
		int getSecondSort();
		int getThirdSort();
		int getForthSort();
		int getFifthSort();

		void setFirstSort(int value);
		void setSecondSort(int value);
		void setThirdSort(int value);
		void setFourthSort(int value);
		void setFifthSort(int value);
};
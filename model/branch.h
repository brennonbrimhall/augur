class Branch {
	private:
		double probability;
		Team[] teams;
	public:
		void sort();
		Team findTeam(int teamNumber);
};
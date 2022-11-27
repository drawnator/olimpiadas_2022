#include <iostream>

using namespace std;
int jackpots;

bool on_circle(float x, float y)
{
	float formula;
	formula = pow(x, 2) + pow(y, 2);
	if (formula < 1) { return true; }
	else if (formula > 1) { return false; }
	else { jackpots += 1; return false; }
}

int main()
{
	int count, n_testes;
	jackpots = count = 0;
	n_testes = 1;
	while (true) {
		count = 0;
		for (int i = 0; i < n_testes; i++) {
			if (on_circle((float)rand() / (float)RAND_MAX, (float)rand() / (float)RAND_MAX)) { count += 1; }
		}
		cout <<"\rjackpots = " << jackpots << " testes = " << n_testes << " pi = " << 4 * (float)count / (float)n_testes;
		n_testes += 1;
	}
}

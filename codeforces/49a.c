#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>

#define MAX_LENGTH 100

bool is_vowel(char c)
{
	c = tolower(c);

	return (c == 'a' || c == 'e' || c == 'i'
		|| c == 'o' || c == 'u' || c == 'y');
}

int main()
{
	char question[MAX_LENGTH];
	scanf("%[^\n]s", question);

	bool result = false;
	for (int i = 0; question[i] != 0 && question[i] != '?'; i++) {
		if (isalpha(question[i])) {
			result = is_vowel(question[i]);
		}
	}

	printf(result ? "YES" : "NO");

	return 0;
}

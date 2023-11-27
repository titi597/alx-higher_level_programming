#include "lists.h"

/**
 * check_cycle - checking whether a singly linked list has a cycle
 * @list: pointer to an array
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *rapid = list;

	while (slow != NULL && rapid != NULL && rapid->next != NULL)
	{
		slow = slow->next;
		rapid = rapid->next->next;

		if (slow == rapid)
			return (1);
	}
	return (0);
}

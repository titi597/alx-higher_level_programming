#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checking if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *temp;

	if (*head == NULL || (*head)->next == NULL)
        return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		/* Reverse the first half of the list */
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}
	/* If the list has odd number of elements, move slow to next node */
	if (fast != NULL)
		slow = slow->next;
	/* Compare the reversed first half with the second half */
	while (slow != NULL)
	{
		if (prev->n != slow->n)
			return (0);
		prev = prev->next;
		slow = slow->next;
	}
	return (1);
}


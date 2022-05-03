#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
 * aux - main
 * @start: list
 * @end: list
 * Return: 1 or 0
 */

int aux(listint_t **start, listint_t *end)
{
	int flag;

	if (!end)
		return (1);
	if (aux(start, end->next))
		flag = 1;
	else
		flag = 0;
	if (flag == 0)
		return (0);
	if (end->n == (*start)->n)
		flag = 1;
	else
		flag = 0;
	*start = (*start)->next;
	return (flag);
}

/**
 * is_palindrome - main
 * @head: list
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	return (aux(head, *head));
}

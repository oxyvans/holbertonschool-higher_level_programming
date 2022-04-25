#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - frees a listint_t list
 * @list: pointer to list to be freed
 * Return: 0 if there is no cycle, 1 if there is a cycl
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_p, *fast_p;

	if (!list || !list->next)
		return (0);

	fast_p = list->next->next;
	slow_p = list->next;

	while (slow_p && fast_p && fast_p->next)
	{
		if (slow_p == fast_p)
			return (1);

		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
	}

	return (0);
}

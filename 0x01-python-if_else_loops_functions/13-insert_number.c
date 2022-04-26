#include "lists.h"

/**
 * insert_node - inserts
 * @head: pointer
 * @number: int
 * Return: list
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *aux = *head;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;

	if (!aux || aux->n >= number)
	{
		new->next = aux;
		*head = new;
		return (new);
	}

	while (aux && aux->next && aux->next->n < number)
		aux = aux->next;

	new->next = aux->next;
	aux->next = new;

	return (new);
}

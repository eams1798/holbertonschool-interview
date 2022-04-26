#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 *
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else if (new->n < current->n)
	{
		*head = new;
		new->next = current;
	}
	else
	{
		for (; current != NULL; current = current->next)
		{
			if (current->next == NULL)
			{
				current->next = new;
				break;
			}
			if (new->n < current->next->n)
			{
				new->next = current->next;
				current->next = new;
				break;
			}
		}
	}
	return (new);
}

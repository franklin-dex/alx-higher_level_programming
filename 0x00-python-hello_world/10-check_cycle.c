#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *quick;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list->next;
	quick = list->next->next;

	while (slow && quick && quick->next)
	{
		if (slow == quick)
			return (1);

		slow = slow->next;
		quick = quick->next->next;
	}

	return (0);
}

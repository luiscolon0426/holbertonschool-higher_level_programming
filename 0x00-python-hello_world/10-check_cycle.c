#include "lists.h"
/**
 * check_cycle - checks if the linked list
 * has a cycle
 * @list: single linked list
 * Return: 0 if cycle doesnt exist, 1 if exist
 **/

int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	if (list == NULL || list->next == NULL)
		return (0);

	fast = list->next->next;
	slow = list->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}

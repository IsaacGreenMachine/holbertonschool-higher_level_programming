#include "lists.h"
/**
 * is_palindrome - checks if linked list is palindrome
 * @head: start of a listint
 * Return: 0 if not, 1 if is
 */
int is_palindrome(listint_t **head)
{
listint_t *current;
int pos = 0, stat = -1;
if (head == NULL || *head == NULL)
return (1);
current = *head;
while (current->next != NULL) 
{
/*check for even*/
if (current->n == current->next->n)
stat = checkPal(*head, pos, pos + 1);

/*check for odd*/
if (current->next->next != NULL)
{
if (current->n == current->next->next->n)
stat = checkPal(*head, pos, pos + 2);
}
if (stat == 1)
return (1);

if (current == NULL)
return (0);

current = current->next;
pos++;
}
return (0);
}

/**
 * getNode - gets the node at a specified index
 * @head: start of a listint
 * @index: desired node of a listint
 * Return: pointer to desired node or NULL if failed
 */
listint_t *getNode(listint_t *head, unsigned int index)
{
listint_t *node = head;
for (; node != NULL && index != 0; index--, node = node->next)
{
}
if (node == NULL)
return (NULL);
else
return (node);
}

/**
 * checkPal - checks a palindrome from two positions
 * @head: head of list
 * @pos1: first position
 * @pos2: second position
 * Return: 0 if not, 1 if is
 */
int checkPal(listint_t *head, int pos1, int pos2)
{
listint_t *n1 = getNode(head, pos1), *n2 = getNode(head, pos2);
while (pos1 != 0 && n2 != NULL)
{
pos1--, pos2++;
n1 = getNode(head, pos1);
n2 = n2->next;
if (n1->n != n2->n)
return (0);
}
if (n1->n != n2->n)
return (0);
else
return (1);
}

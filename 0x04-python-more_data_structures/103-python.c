#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - function that prints list
 * @p: pointer to an array
 */
void print_python_list(PyObject *p)
{
	long intsize, i;
	PyListObject *list;
	PyObject *item;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((item)->ob_type)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
/**
 * print_python_bytes - function that prints bytes
 * @p: pointer to an array
 */
void print_python_bytes(PyObject *p) 
{
	long int size, i, apt;
	char *bytes;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)(p))->ob_size;
	bytes = ((PyBytesObject *)p)->ob_sval;

	printf("  Size: %ld\n", size);
	printf("  trying string: %s\n", bytes);

	if (size >= 10)
		apt = 10;
	else
		apt = size + 1;

	printf("  first %ld bytes:", apt);

	for (i = 0; i < apt;; i++)
	{
		if (bytes[i] > 0)
			printf(" %02x", bytes[i]);
		else
			printf(" %02x", 256 + bytes[i]);
	}
	printf("\n");
}

#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - function that prints list
 * @p: pointer to an array
 */
void print_python_list(PyObject *p)
{
	long int size, allocate, j;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	allocate = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);

	for (j = 0; j < size; j++)
	{
		type = list->ob_item[j]->ob_type->tp_name;
		printf("Element %d: %s\n", j, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[j]);
	}
}
/**
 * print_python_bytes - function that prints bytes
 * @p: pointer to an array
 */
void print_python_bytes(PyObject *p)
{
	unsigned char size, j;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");

	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  Size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", size);

	for (j = 0; j < size; j++)
	{
		printf("%02hhx", bytes->ob_sval[j]);

		if (j == (size - 1))
			print("\n");
		else
			printf(" ");
	}
}

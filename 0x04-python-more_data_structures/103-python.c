#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - function that will list
 * @p: pointer to an array
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
/**
 * print_python_bytes - function that will print bytes
 * @p: pointer to an array
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *bytes;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	bytes = PyBytes_AsString(p);
	printf("  Size: %zd\n", size);
	printf("  trying string: %s\n", bytes);
	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx", bytes[i]);
		if (i < 9)
			printf(" ");
	}
	printf("\n");
}

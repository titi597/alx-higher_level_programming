#include <Python.h>
/**
 * print_python_list -function that prints list
 * @p: pointer to an array
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *element;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List: %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	size = PyList_Size(p);
	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	}
}
/**
 * print_python_bytes - function that prints bytes
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

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes);

	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx", bytes[i]);
		if (i < 9)
		{
			printf(" ");
		}
	}
	printf("\n");
}

#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - function that prints list
 * @p: pointer to an array
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid List Object\n");
		return;
	}
	size = Py_SIZE(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
/**
 * print_python_list - function that prints bytes
 * @p: pointer to an array
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = PyBytes_Size(p);
	char *str = PyBytes_AsString(p);

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid Bytes Object\n");
		return;
	}
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str ? str : "(no value)");

	printf("  first 10 bytes: ");
	for (Py_ssize_t i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx", str[i]);
		if (i + 1 < size && i + 1 < 10)
		{
			printf(" ");
		}
	}
	printf("\n");
}
/**
 * print_python_list - function that prints float
 * @p: pointer to an array
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "Invalid Float Object\n");
		return;
	}
	printf("[.] float object info\n");
	printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}

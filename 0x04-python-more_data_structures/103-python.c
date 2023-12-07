#include <stdio.h>
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
	printf("[*] Size of the Python List: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	size = ((PyVarObject *)p)->ob_size;
	for (i = 0; i < size; i++)
	{
		if (PySequence_Check(p))
		{
			element = PyObject_GetItem(p, PyLong_FromSsize_t(i));
			if (element == NULL)
			{
				PyErr_Print();
				return;
			}
			printf("Element %ld: %s\n", i, element->ob_type->tp_name);
			Py_DECREF(element);
		}
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
	size = ((PyVarObject *)p)->ob_size;
	bytes = ((PyBytesObject *)p)->ob_sval;

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

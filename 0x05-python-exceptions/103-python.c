#include <Python.h>
#include <stdio.h>
/**
 * print_python_float - function that prints float
 * @p: pointer to an array
 */
void print_python_float(PyObject *p)
{
	double aptr = 0;
	char *strings = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	aptr = ((PyFloatObject *)p)->ob_fval;
	strings = PyOS_double_to_string(aptr, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", strings);
}
/**
 * print_python_bytes - function that prints bytes
 * @p: pointer to an array
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t dsize = 0, i = 0;
	char *strings = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	dsize = PyBytes_Size(p);
	printf("  size: %zd\n", dsize);
	strings = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", strings);
	printf("  first %zd bytes:", dsize < 10 ? dsize + 1 : 10);
	while (i < dsize + 1 && i < 10)
	{
		printf(" %02hhx", strings[i]);
		i++;
	}
	printf("\n");
}
/**
 * print_python_list - function that prints lists
 * @p: pointer to an array
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t dsize = 0;
	PyObject *objects;
	int k = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		dsize = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", dsize);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (k < dsize)
		{
			objects = PyList_GET_ITEM(p, k);
			printf("Element %d: %s\n", k, objects->ob_type->tp_name);
			if (PyBytes_Check(objects))
				print_python_bytes(objects);
			else if (PyFloat_Check(objects))
				print_python_float(objects);
			k++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}

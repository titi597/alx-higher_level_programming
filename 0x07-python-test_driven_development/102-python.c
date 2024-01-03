#define PY_SSIZE_T_CLEAN
#include <Python.h>
/**
 * print_python_string - function that prints Python strings.
 * @p: pointer to an array p
 */
void print_python_string(PyObject *p)
{
	const char *str;

	if (!PyUnicode_Check(p))
	{
		fprintf(stderr, "Invalid String Object\n");
		return;
	}
	Py_ssize_t size = PyUnicode_GET_SIZE(p);

	str = PyUnicode_AsUTF8(p);

	printf("String data: %s\n", str);
	printf("Address of the object: %p\n", (void *)p);
	printf("Size: %zd\n", size);
	printf("Unicode object address: %p\n", (void *)PyUnicode_DATA(p));
}

#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - Prints information about a Python list object
 * @p: A PyObject pointer to the list object
 */
void print_python_list(PyObject *p) {
		Py_ssize_t size, i;
		PyObject *item;

		if (!PyList_Check(p)) {
				printf("[ERROR] Invalid List Object\n");
				return;
		}

		size = PyList_Size(p);

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

		for (i = 0; i < size; i++) {
				printf("Element %zd: ", i);
				item = PyList_GetItem(p, i);

				if (PyBytes_Check(item)) {
						print_python_bytes(item);
				} else {
						printf("%s\n", Py_TYPE(item)->tp_name);
				}
		}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: A PyObject pointer to the bytes object
 */
void print_python_bytes(PyObject *p) {
		Py_ssize_t size, i;
		char *bytes;

		if (!PyBytes_Check(p)) {
				printf("[ERROR] Invalid Bytes Object\n");
				return;
		}

		size = PyBytes_Size(p);
		bytes = PyBytes_AsString(p);

		printf("[.] bytes object info\n");
		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", bytes);
		printf("  first %zd bytes: ", size < 10 ? size : 10);

		for (i = 0; i < size && i < 10; i++) {
				printf("%02x ", bytes[i]);
		}
		printf("\n");
}

/**
 * main - Entry point for testing the Python object info functions
 *
 * Return: Always 0 (success)
 */
int main(void) {
		// Add your test cases here as described in the provided Python script
		return 0;
}


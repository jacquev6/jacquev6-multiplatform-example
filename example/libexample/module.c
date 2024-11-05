#define PY_SSIZE_T_CLEAN
#include <Python.h>


static PyObject* add(PyObject* self, PyObject* args) {
  long a, b;
  if (PyArg_ParseTuple(args, "ll", &a, &b)) {
    return PyLong_FromLong(a + b);
  } else {
    return NULL;
  }
}

static PyMethodDef methods[] = {
  {"add",  add, METH_VARARGS, NULL},
  {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
  PyModuleDef_HEAD_INIT,
  "libexample",
  NULL,
  -1,
  methods
};

PyMODINIT_FUNC PyInit_libexample(void) {
  return PyModule_Create(&module);
}

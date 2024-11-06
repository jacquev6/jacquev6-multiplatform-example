#define PY_SSIZE_T_CLEAN
#include <Python.h>


// extern "C"
static PyObject* add(PyObject* self, PyObject* args) {
  long a, b;
  if (PyArg_ParseTuple(args, "ll", &a, &b)) {
    char* cells = (char*)malloc(a + b);

    #pragma omp parallel for
    for (int i = 0; i < a + b; i++) {
      cells[i] = 1;
    }

    long r = 0;
    for (int i = 0; i < a + b; i++) {
      r += cells[i];
    }

    free(cells);

    return PyLong_FromLong(r);
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

import actionCreator from '../../libs/actionCreator'
import axios from '../../libs/axios'

const solveAction = actionCreator('hello')

const SET_FIELD = solveAction('SET_FIELD')
const RUN_TEST = solveAction('RUN_TEST', true)
const SUBMIT = solveAction('RUN_TEST', true)

let initialState = {
  // Editor
  code: '',

  // Result
  loading: false,
  error: {},
  result: {}
}

export default (state = initialState, action) => {
  switch (action.type) {
    // -------------------
    //       COMMON
    // -------------------
    case SET_FIELD:
      return {
        ...state,
        [action.field]: action.value
      }
    // ---------------------
    //  RUN TEST AND SUBMIT
    // ---------------------
    case RUN_TEST.PENDING:
    case SUBMIT.PENDING:
      return {
        ...state,
        loading: true
      }
    case RUN_TEST.RESOLVED:
      return {
        ...state,
        loading: false,
        result: action.payload
      }
    case SUBMIT.RESOLVED:
      return {
        ...state,
        loading: false,
        result: action.payload
      }
    case RUN_TEST.REJECTED:
    case SUBMIT.REJECTED:
      return {
        ...state,
        loading: false,
        error: action.error

      }
    default: return state
  }
}

export const actions = {
  setField: (field, value) => ({
    type: SET_FIELD,
    field,
    value
  }),
  runTest: (taskID, code) => {
    const formData = {
      taskID,
      code
    }

    return {
      type: RUN_TEST,
      promise: axios.post('/solve/run-test', formData)
        .then(resp => console.log(resp.data.result))
    }
  },
  submit: (taskID, code) => {
    const formData = {
      taskID,
      code
    }

    return {
      type: SUBMIT,
      promise: axios.post('/solve/submit', formData)
    }
  }
}

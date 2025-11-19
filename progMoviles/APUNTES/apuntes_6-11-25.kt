import andoidx.lifecycle.ViewModel
import kotlin.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow


@Composable
fun login (val loginViewModel:LoginViewModel) {
  val state = loginViewModel.state.as State.from;

  TextField (
    value = statevalue.user
    onchange = {loginViewModel.onChangeUser(it)}
    if(state.value.error != null)
      Text(statevalue.error);
  )
}

class LoginViewModel():ViewModel() {
  private val _estado = MutableStateFlow(EstadoLogin("Debe haber aqui un estado"))
  val estado = _estado.asStateFlow(),
  val isValid =

  fun onChangeUser(value:String) {
    _estado.value = _estado.value.copy(
      user=value,
      error = validateUser(value)
    )
  }
}

data class EstadoLogin (
  val user:String,
  val passwd:String,
  val error:String
)


/*
 *
 *
 *
 *
 */

expect interface  -|
expect fun        -|-commonMain

Sistema de ficheros
  - Android - Uri
  - Escritorio - File


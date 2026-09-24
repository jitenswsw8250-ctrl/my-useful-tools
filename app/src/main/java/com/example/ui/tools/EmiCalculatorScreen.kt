package com.example.ui.tools

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import java.text.NumberFormat
import java.util.Locale
import kotlin.math.pow

@Composable
fun EmiCalculatorScreen(modifier: Modifier = Modifier) {
  var principalStr by rememberSaveable { mutableStateOf("1000000") }
  var rateStr by rememberSaveable { mutableStateOf("8.5") }
  var tenureStr by rememberSaveable { mutableStateOf("20") }
  var emiResult by rememberSaveable { mutableStateOf<String?>(null) }
  var totalInterestResult by rememberSaveable { mutableStateOf<String?>(null) }

  fun calculate() {
    val p = principalStr.toDoubleOrNull() ?: 0.0
    val rYear = rateStr.toDoubleOrNull() ?: 0.0
    val tYears = tenureStr.toDoubleOrNull() ?: 0.0
    if (p > 0 && rYear > 0 && tYears > 0) {
      val rMonth = rYear / 12.0 / 100.0
      val nMonths = tYears * 12.0
      val emi = (p * rMonth * (1 + rMonth).pow(nMonths)) / ((1 + rMonth).pow(nMonths) - 1)
      val totalPayable = emi * nMonths
      val totalInterest = totalPayable - p
      val inrFormat = NumberFormat.getCurrencyInstance(Locale("en", "IN"))
      emiResult = inrFormat.format(emi)
      totalInterestResult = inrFormat.format(totalInterest)
    }
  }

  Column(modifier = modifier.fillMaxWidth().padding(16.dp)) {
    Card(
      shape = RoundedCornerShape(16.dp),
      colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface),
      modifier = Modifier.fillMaxWidth()
    ) {
      Column(modifier = Modifier.padding(20.dp)) {
        Text("EMI Loan Calculator", style = MaterialTheme.typography.headlineSmall, fontWeight = FontWeight.Bold)
        Spacer(modifier = Modifier.height(12.dp))
        OutlinedTextField(
          value = principalStr,
          onValueChange = { principalStr = it },
          label = { Text("Loan Amount (₹)") },
          keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
          modifier = Modifier.fillMaxWidth().testTag("emi_amount_input")
        )
        Spacer(modifier = Modifier.height(8.dp))
        OutlinedTextField(
          value = rateStr,
          onValueChange = { rateStr = it },
          label = { Text("Interest Rate (% per annum)") },
          keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal),
          modifier = Modifier.fillMaxWidth().testTag("emi_rate_input")
        )
        Spacer(modifier = Modifier.height(8.dp))
        OutlinedTextField(
          value = tenureStr,
          onValueChange = { tenureStr = it },
          label = { Text("Tenure (Years)") },
          keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
          modifier = Modifier.fillMaxWidth().testTag("emi_tenure_input")
        )
        Spacer(modifier = Modifier.height(12.dp))
        Button(
          onClick = { calculate() },
          modifier = Modifier.fillMaxWidth().testTag("emi_calculate_button")
        ) {
          Text("Calculate EMI")
        }

        if (emiResult != null) {
          Spacer(modifier = Modifier.height(16.dp))
          Text("Monthly EMI: ${emiResult}", fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.primary)
          Text("Total Interest: ${totalInterestResult}", color = MaterialTheme.colorScheme.onSurfaceVariant)
        }
      }
    }
  }
}

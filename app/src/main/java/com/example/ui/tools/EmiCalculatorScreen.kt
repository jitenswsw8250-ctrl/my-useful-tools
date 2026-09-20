package com.example.ui.tools

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Calculate
import androidx.compose.material.icons.filled.Clear
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.FilterChip
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Slider
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.derivedStateOf
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.ui.components.AdSensePlaceholder
import com.example.ui.theme.Emerald600
import com.example.ui.theme.Rose600
import kotlin.math.pow

@Composable
fun EmiCalculatorScreen(modifier: Modifier = Modifier) {
  var loanAmountStr by rememberSaveable { mutableStateOf("50000") }
  var interestRateStr by rememberSaveable { mutableStateOf("8.5") }
  var tenureStr by rememberSaveable { mutableStateOf("5") }
  var isTenureInYears by rememberSaveable { mutableStateOf(true) }
  var selectedCurrency by rememberSaveable { mutableStateOf("INR") } // "INR" or "USD"
  val currencySymbol = if (selectedCurrency == "INR") "₹" else "$"

  // Calculation
  val emiResult by remember {
    derivedStateOf {
      val principal = loanAmountStr.toDoubleOrNull() ?: 0.0
      val annualRate = interestRateStr.toDoubleOrNull() ?: 0.0
      val tenureVal = tenureStr.toDoubleOrNull() ?: 0.0

      val months = if (isTenureInYears) tenureVal * 12 else tenureVal

      if (principal <= 0 || annualRate <= 0 || months <= 0) {
        null
      } else {
        val monthlyRate = annualRate / (12 * 100)
        val emi = (principal * monthlyRate * (1 + monthlyRate).pow(months)) /
            ((1 + monthlyRate).pow(months) - 1)
        val totalPayment = emi * months
        val totalInterest = totalPayment - principal

        val principalPercent = (principal / totalPayment) * 100
        val interestPercent = (totalInterest / totalPayment) * 100

        EmiCalculation(
          monthlyEmi = emi,
          totalInterest = totalInterest,
          totalPayment = totalPayment,
          principal = principal,
          principalPercent = principalPercent.toFloat(),
          interestPercent = interestPercent.toFloat()
        )
      }
    }
  }

  Column(
    modifier = modifier
      .fillMaxWidth()
      .padding(16.dp)
  ) {
    Text(
      text = "EMI Calculator",
      style = MaterialTheme.typography.headlineMedium,
      fontWeight = FontWeight.Bold,
      color = MaterialTheme.colorScheme.onBackground
    )
    Text(
      text = "Calculate your monthly Equated Monthly Installment (EMI), total interest, and total repayment for home, car, or personal loans.",
      style = MaterialTheme.typography.bodyMedium,
      color = MaterialTheme.colorScheme.onSurfaceVariant,
      modifier = Modifier.padding(top = 4.dp, bottom = 12.dp)
    )

    AdSensePlaceholder(slotLabel = "AdSense Responsive Slot - EMI Tool Top")

    Card(
      modifier = Modifier
        .fillMaxWidth()
        .padding(vertical = 8.dp),
      colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface),
      elevation = CardDefaults.cardElevation(defaultElevation = 2.dp),
      shape = RoundedCornerShape(16.dp)
    ) {
      Column(modifier = Modifier.padding(16.dp)) {
        // Currency Selector
        Column(modifier = Modifier.fillMaxWidth()) {
          Text(
            text = "Select Currency",
            style = MaterialTheme.typography.labelMedium,
            fontWeight = FontWeight.SemiBold,
            color = MaterialTheme.colorScheme.onSurfaceVariant
          )

          Spacer(modifier = Modifier.height(6.dp))

          Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.spacedBy(8.dp)
          ) {
            FilterChip(
              selected = selectedCurrency == "INR",
              onClick = { selectedCurrency = "INR" },
              label = { Text("Indian Rupee (₹ INR)") },
              modifier = Modifier.testTag("currency_inr_chip")
            )
            FilterChip(
              selected = selectedCurrency == "USD",
              onClick = { selectedCurrency = "USD" },
              label = { Text("US Dollar ($ USD)") },
              modifier = Modifier.testTag("currency_usd_chip")
            )
          }
        }

        Spacer(modifier = Modifier.height(16.dp))

        // Loan Amount Input
        OutlinedTextField(
          value = loanAmountStr,
          onValueChange = { loanAmountStr = it },
          label = { Text("Loan Amount ($currencySymbol)") },
          placeholder = { Text("e.g. 50000") },
          leadingIcon = { Text(currencySymbol, fontWeight = FontWeight.Bold) },
          keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
          singleLine = true,
          modifier = Modifier
            .fillMaxWidth()
            .testTag("loan_amount_input")
        )

        Spacer(modifier = Modifier.height(16.dp))

        // Interest Rate Input
        OutlinedTextField(
          value = interestRateStr,
          onValueChange = { interestRateStr = it },
          label = { Text("Interest Rate (% per annum)") },
          placeholder = { Text("e.g. 8.5") },
          trailingIcon = { Text("%", fontWeight = FontWeight.Bold, modifier = Modifier.padding(end = 12.dp)) },
          keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal),
          singleLine = true,
          modifier = Modifier
            .fillMaxWidth()
            .testTag("interest_rate_input")
        )

        Spacer(modifier = Modifier.height(16.dp))

        // Loan Tenure Input & Toggle (Years / Months)
        Row(
          modifier = Modifier.fillMaxWidth(),
          horizontalArrangement = Arrangement.spacedBy(8.dp),
          verticalAlignment = Alignment.CenterVertically
        ) {
          OutlinedTextField(
            value = tenureStr,
            onValueChange = { tenureStr = it },
            label = { Text("Loan Tenure") },
            placeholder = { Text("e.g. 5") },
            keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
            singleLine = true,
            modifier = Modifier
              .weight(1f)
              .testTag("tenure_input")
          )

          Row(horizontalArrangement = Arrangement.spacedBy(4.dp)) {
            FilterChip(
              selected = isTenureInYears,
              onClick = { isTenureInYears = true },
              label = { Text("Years") },
              modifier = Modifier.testTag("tenure_years_chip")
            )
            FilterChip(
              selected = !isTenureInYears,
              onClick = { isTenureInYears = false },
              label = { Text("Months") },
              modifier = Modifier.testTag("tenure_months_chip")
            )
          }
        }

        Spacer(modifier = Modifier.height(20.dp))

        // Action Row
        Row(
          modifier = Modifier.fillMaxWidth(),
          horizontalArrangement = Arrangement.spacedBy(12.dp)
        ) {
          Button(
            onClick = { /* reactive recalculation triggers automatically via derivedStateOf */ },
            modifier = Modifier
              .weight(1f)
              .height(48.dp)
              .testTag("calculate_emi_button")
          ) {
            Icon(Icons.Default.Calculate, contentDescription = null, modifier = Modifier.size(18.dp))
            Spacer(modifier = Modifier.width(6.dp))
            Text("Calculate EMI")
          }

          OutlinedButton(
            onClick = {
              selectedCurrency = "INR"
              loanAmountStr = "50000"
              interestRateStr = "8.5"
              tenureStr = "5"
              isTenureInYears = true
            },
            modifier = Modifier
              .height(48.dp)
              .testTag("clear_emi_button")
          ) {
            Icon(Icons.Default.Clear, contentDescription = null, modifier = Modifier.size(18.dp))
            Spacer(modifier = Modifier.width(6.dp))
            Text("Reset")
          }
        }
      }
    }

    // Results Box
    emiResult?.let { result ->
      Spacer(modifier = Modifier.height(16.dp))

      Card(
        modifier = Modifier
          .fillMaxWidth()
          .testTag("emi_result_card"),
        colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.primaryContainer),
        shape = RoundedCornerShape(16.dp)
      ) {
        Column(
          modifier = Modifier.padding(20.dp),
          horizontalAlignment = Alignment.CenterHorizontally
        ) {
          Text(
            text = "MONTHLY EMI",
            style = MaterialTheme.typography.labelMedium,
            fontWeight = FontWeight.Bold,
            color = MaterialTheme.colorScheme.onPrimaryContainer.copy(alpha = 0.8f),
            letterSpacing = 1.2.sp
          )

          Spacer(modifier = Modifier.height(4.dp))

          Text(
            text = formatEmiAmount(result.monthlyEmi, selectedCurrency),
            style = MaterialTheme.typography.headlineLarge,
            fontWeight = FontWeight.Black,
            color = MaterialTheme.colorScheme.primary
          )

          Spacer(modifier = Modifier.height(16.dp))

          // Total Interest & Total Payment
          Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.spacedBy(12.dp)
          ) {
            EmiStatCard(
              title = "Total Interest",
              amount = formatEmiAmount(result.totalInterest, selectedCurrency),
              color = Rose600,
              modifier = Modifier.weight(1f)
            )

            EmiStatCard(
              title = "Total Payment",
              amount = formatEmiAmount(result.totalPayment, selectedCurrency),
              color = MaterialTheme.colorScheme.primary,
              modifier = Modifier.weight(1f)
            )
          }

          Spacer(modifier = Modifier.height(16.dp))

          // Breakdown Visual Bar
          Column(
            modifier = Modifier
              .fillMaxWidth()
              .clip(RoundedCornerShape(12.dp))
              .background(MaterialTheme.colorScheme.surface)
              .padding(16.dp)
          ) {
            Text(
              text = "Breakdown of Total Payment",
              style = MaterialTheme.typography.titleSmall,
              fontWeight = FontWeight.Bold
            )

            Spacer(modifier = Modifier.height(10.dp))

            // Visual Progress Bar (Principal vs Interest)
            Box(
              modifier = Modifier
                .fillMaxWidth()
                .height(16.dp)
                .clip(RoundedCornerShape(8.dp))
                .background(Rose600)
            ) {
              Box(
                modifier = Modifier
                  .fillMaxHeight()
                  .fillMaxWidth(fraction = (result.principalPercent / 100f).coerceIn(0f, 1f))
                  .background(Emerald600)
              )
            }

            Spacer(modifier = Modifier.height(10.dp))

            Row(
              modifier = Modifier.fillMaxWidth(),
              horizontalArrangement = Arrangement.SpaceBetween
            ) {
              Row(verticalAlignment = Alignment.CenterVertically) {
                Box(modifier = Modifier.size(10.dp).clip(CircleShape).background(Emerald600))
                Spacer(modifier = Modifier.width(6.dp))
                Text(
                  text = "Principal: %.1f%%".format(result.principalPercent),
                  style = MaterialTheme.typography.bodySmall,
                  fontWeight = FontWeight.Medium
                )
              }

              Row(verticalAlignment = Alignment.CenterVertically) {
                Box(modifier = Modifier.size(10.dp).clip(CircleShape).background(Rose600))
                Spacer(modifier = Modifier.width(6.dp))
                Text(
                  text = "Interest: %.1f%%".format(result.interestPercent),
                  style = MaterialTheme.typography.bodySmall,
                  fontWeight = FontWeight.Medium
                )
              }
            }
          }
        }
      }
    }

    Spacer(modifier = Modifier.height(16.dp))
    AdSensePlaceholder(slotLabel = "AdSense Responsive Slot - EMI Tool Bottom")
  }
}

@Composable
private fun EmiStatCard(title: String, amount: String, color: androidx.compose.ui.graphics.Color, modifier: Modifier = Modifier) {
  Column(
    modifier = modifier
      .clip(RoundedCornerShape(12.dp))
      .background(MaterialTheme.colorScheme.surface)
      .padding(14.dp),
    horizontalAlignment = Alignment.CenterHorizontally
  ) {
    Text(
      text = title,
      style = MaterialTheme.typography.labelSmall,
      color = MaterialTheme.colorScheme.onSurfaceVariant
    )
    Spacer(modifier = Modifier.height(4.dp))
    Text(
      text = amount,
      style = MaterialTheme.typography.titleMedium,
      fontWeight = FontWeight.Bold,
      color = color
    )
  }
}

data class EmiCalculation(
  val monthlyEmi: Double,
  val totalInterest: Double,
  val totalPayment: Double,
  val principal: Double,
  val principalPercent: Float,
  val interestPercent: Float
)

private fun formatEmiAmount(amount: Double, currency: String): String {
  val symbol = if (currency == "INR") "₹" else "$"
  return if (currency == "INR") {
    "$symbol${formatIndianGrouping(amount)}"
  } else {
    val df = java.text.DecimalFormat("#,##0.00")
    "$symbol${df.format(amount)}"
  }
}

private fun formatIndianGrouping(value: Double): String {
  val rounded = String.format(java.util.Locale.US, "%.2f", value)
  val parts = rounded.split(".")
  var integerPart = parts[0]
  val decimalPart = parts[1]
  val isNegative = integerPart.startsWith("-")
  if (isNegative) {
    integerPart = integerPart.substring(1)
  }
  val result = if (integerPart.length > 3) {
    val lastThree = integerPart.substring(integerPart.length - 3)
    val remaining = integerPart.substring(0, integerPart.length - 3)
    val sb = StringBuilder()
    var count = 0
    for (i in remaining.length - 1 downTo 0) {
      sb.append(remaining[i])
      count++
      if (count % 2 == 0 && i > 0) sb.append(',')
    }
    "${sb.reverse()},$lastThree.$decimalPart"
  } else {
    "$integerPart.$decimalPart"
  }
  return if (isNegative) "-$result" else result
}

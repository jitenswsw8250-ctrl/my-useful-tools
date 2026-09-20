package com.example.ui.tools

import android.content.ClipData
import android.content.ClipboardManager
import android.content.Context
import android.widget.Toast
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Clear
import androidx.compose.material.icons.filled.ContentCopy
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Tab
import androidx.compose.material3.TabRow
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.derivedStateOf
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.ui.components.AdSensePlaceholder
import com.example.ui.theme.Emerald600
import com.example.ui.theme.Rose600

@Composable
fun PercentageCalculatorScreen(modifier: Modifier = Modifier) {
  val context = LocalContext.current
  var selectedTab by rememberSaveable { mutableIntStateOf(0) }

  // Mode 1: What is X% of Y?
  var m1Percent by rememberSaveable { mutableStateOf("15") }
  var m1Total by rememberSaveable { mutableStateOf("250") }

  // Mode 2: Percentage Increase / Decrease from X to Y
  var m2Initial by rememberSaveable { mutableStateOf("100") }
  var m2Final by rememberSaveable { mutableStateOf("140") }

  // Mode 3: X is what % of Y?
  var m3Part by rememberSaveable { mutableStateOf("45") }
  var m3Whole by rememberSaveable { mutableStateOf("60") }

  val tabs = listOf("X% of Y", "Change %", "X is % of Y")

  Column(
    modifier = modifier
      .fillMaxWidth()
      .padding(16.dp)
  ) {
    Text(
      text = "Percentage Calculator",
      style = MaterialTheme.typography.headlineMedium,
      fontWeight = FontWeight.Bold,
      color = MaterialTheme.colorScheme.onBackground
    )
    Text(
      text = "Simple and fast percentage calculations: find percentages of numbers, percentage change (increase or decrease), and proportions.",
      style = MaterialTheme.typography.bodyMedium,
      color = MaterialTheme.colorScheme.onSurfaceVariant,
      modifier = Modifier.padding(top = 4.dp, bottom = 12.dp)
    )

    AdSensePlaceholder(slotLabel = "AdSense Responsive Slot - Percentage Tool Top")

    // Tabs for 3 Modes
    TabRow(
      selectedTabIndex = selectedTab,
      modifier = Modifier
        .fillMaxWidth()
        .clip(RoundedCornerShape(12.dp))
    ) {
      tabs.forEachIndexed { index, title ->
        Tab(
          selected = selectedTab == index,
          onClick = { selectedTab = index },
          text = { Text(title, fontWeight = if (selectedTab == index) FontWeight.Bold else FontWeight.Normal) },
          modifier = Modifier.testTag("percent_tab_$index")
        )
      }
    }

    Spacer(modifier = Modifier.height(16.dp))

    when (selectedTab) {
      0 -> {
        // Mode 1: What is X% of Y?
        val result by remember {
          derivedStateOf {
            val p = m1Percent.toDoubleOrNull()
            val t = m1Total.toDoubleOrNull()
            if (p != null && t != null) (p / 100.0) * t else null
          }
        }

        PercentageCard(
          title = "Calculate X% of Y",
          subtitle = "Find the exact percentage amount of any base number."
        ) {
          Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.spacedBy(8.dp),
            verticalAlignment = Alignment.CenterVertically
          ) {
            OutlinedTextField(
              value = m1Percent,
              onValueChange = { m1Percent = it },
              label = { Text("What is") },
              trailingIcon = { Text("%", fontWeight = FontWeight.Bold) },
              keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal),
              singleLine = true,
              modifier = Modifier.weight(1f).testTag("m1_percent_input")
            )

            Text("of", fontWeight = FontWeight.SemiBold)

            OutlinedTextField(
              value = m1Total,
              onValueChange = { m1Total = it },
              label = { Text("Number") },
              placeholder = { Text("Total") },
              keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal),
              singleLine = true,
              modifier = Modifier.weight(1.3f).testTag("m1_total_input")
            )
          }

          Spacer(modifier = Modifier.height(16.dp))

          result?.let { res ->
            ResultCard(
              label = "${m1Percent}% of ${m1Total} =",
              value = "%,.2f".format(res),
              onCopy = {
                copyToClipboard(context, "%,.2f".format(res))
              }
            )
          }

          Spacer(modifier = Modifier.height(16.dp))

          OutlinedButton(
            onClick = {
              m1Percent = ""
              m1Total = ""
            },
            modifier = Modifier.align(Alignment.End).testTag("clear_m1_button")
          ) {
            Icon(Icons.Default.Clear, contentDescription = null, modifier = Modifier.size(16.dp))
            Spacer(modifier = Modifier.width(6.dp))
            Text("Clear")
          }
        }
      }

      1 -> {
        // Mode 2: Percentage Increase / Decrease
        val changeResult by remember {
          derivedStateOf {
            val init = m2Initial.toDoubleOrNull()
            val fin = m2Final.toDoubleOrNull()
            if (init != null && fin != null && init != 0.0) {
              val diff = fin - init
              val percentChange = (diff / init) * 100.0
              val isIncrease = diff >= 0
              Triple(diff, percentChange, isIncrease)
            } else null
          }
        }

        PercentageCard(
          title = "Percentage Increase / Decrease",
          subtitle = "Calculate the percentage change from an initial value to a final value."
        ) {
          Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.spacedBy(8.dp)
          ) {
            OutlinedTextField(
              value = m2Initial,
              onValueChange = { m2Initial = it },
              label = { Text("From (Initial)") },
              keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal),
              singleLine = true,
              modifier = Modifier.weight(1f).testTag("m2_initial_input")
            )

            OutlinedTextField(
              value = m2Final,
              onValueChange = { m2Final = it },
              label = { Text("To (Final)") },
              keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal),
              singleLine = true,
              modifier = Modifier.weight(1f).testTag("m2_final_input")
            )
          }

          Spacer(modifier = Modifier.height(16.dp))

          changeResult?.let { (diff, pct, isIncrease) ->
            val color = if (isIncrease) Emerald600 else Rose600
            val directionText = if (isIncrease) "Increase" else "Decrease"
            val arrow = if (isIncrease) "▲" else "▼"

            ResultCard(
              label = "From $m2Initial to $m2Final is a:",
              value = "$arrow %,.2f%% $directionText".format(kotlin.math.abs(pct)),
              secondaryText = "Absolute difference: %,.2f".format(diff),
              valueColor = color,
              onCopy = {
                copyToClipboard(context, "%,.2f%%".format(kotlin.math.abs(pct)))
              }
            )
          }

          Spacer(modifier = Modifier.height(16.dp))

          OutlinedButton(
            onClick = {
              m2Initial = ""
              m2Final = ""
            },
            modifier = Modifier.align(Alignment.End).testTag("clear_m2_button")
          ) {
            Icon(Icons.Default.Clear, contentDescription = null, modifier = Modifier.size(16.dp))
            Spacer(modifier = Modifier.width(6.dp))
            Text("Clear")
          }
        }
      }

      2 -> {
        // Mode 3: X is what % of Y?
        val proportionResult by remember {
          derivedStateOf {
            val part = m3Part.toDoubleOrNull()
            val whole = m3Whole.toDoubleOrNull()
            if (part != null && whole != null && whole != 0.0) {
              (part / whole) * 100.0
            } else null
          }
        }

        PercentageCard(
          title = "X is What % of Y?",
          subtitle = "Find what percentage one number represents of another whole number."
        ) {
          Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.spacedBy(8.dp),
            verticalAlignment = Alignment.CenterVertically
          ) {
            OutlinedTextField(
              value = m3Part,
              onValueChange = { m3Part = it },
              label = { Text("Value (X)") },
              keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal),
              singleLine = true,
              modifier = Modifier.weight(1f).testTag("m3_part_input")
            )

            Text("is what % of", fontWeight = FontWeight.SemiBold)

            OutlinedTextField(
              value = m3Whole,
              onValueChange = { m3Whole = it },
              label = { Text("Total (Y)") },
              keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal),
              singleLine = true,
              modifier = Modifier.weight(1f).testTag("m3_whole_input")
            )
          }

          Spacer(modifier = Modifier.height(16.dp))

          proportionResult?.let { res ->
            ResultCard(
              label = "$m3Part of $m3Whole is:",
              value = "%,.2f%%".format(res),
              onCopy = {
                copyToClipboard(context, "%,.2f%%".format(res))
              }
            )
          }

          Spacer(modifier = Modifier.height(16.dp))

          OutlinedButton(
            onClick = {
              m3Part = ""
              m3Whole = ""
            },
            modifier = Modifier.align(Alignment.End).testTag("clear_m3_button")
          ) {
            Icon(Icons.Default.Clear, contentDescription = null, modifier = Modifier.size(16.dp))
            Spacer(modifier = Modifier.width(6.dp))
            Text("Clear")
          }
        }
      }
    }

    Spacer(modifier = Modifier.height(16.dp))
    AdSensePlaceholder(slotLabel = "AdSense Responsive Slot - Percentage Tool Bottom")
  }
}

@Composable
private fun PercentageCard(
  title: String,
  subtitle: String,
  content: @Composable androidx.compose.foundation.layout.ColumnScope.() -> Unit
) {
  Card(
    modifier = Modifier.fillMaxWidth(),
    colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface),
    elevation = CardDefaults.cardElevation(defaultElevation = 2.dp),
    shape = RoundedCornerShape(16.dp)
  ) {
    Column(modifier = Modifier.padding(16.dp)) {
      Text(text = title, style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.Bold)
      Text(
        text = subtitle,
        style = MaterialTheme.typography.bodySmall,
        color = MaterialTheme.colorScheme.onSurfaceVariant
      )
      Spacer(modifier = Modifier.height(16.dp))
      content()
    }
  }
}

@Composable
private fun ResultCard(
  label: String,
  value: String,
  secondaryText: String? = null,
  valueColor: androidx.compose.ui.graphics.Color = MaterialTheme.colorScheme.primary,
  onCopy: () -> Unit
) {
  Box(
    modifier = Modifier
      .fillMaxWidth()
      .clip(RoundedCornerShape(12.dp))
      .background(MaterialTheme.colorScheme.primaryContainer.copy(alpha = 0.6f))
      .padding(16.dp)
  ) {
    Row(
      modifier = Modifier.fillMaxWidth(),
      horizontalArrangement = Arrangement.SpaceBetween,
      verticalAlignment = Alignment.CenterVertically
    ) {
      Column(modifier = Modifier.weight(1f)) {
        Text(
          text = label,
          style = MaterialTheme.typography.bodyMedium,
          color = MaterialTheme.colorScheme.onSurfaceVariant
        )
        Spacer(modifier = Modifier.height(4.dp))
        Text(
          text = value,
          style = MaterialTheme.typography.headlineMedium,
          fontWeight = FontWeight.Black,
          color = valueColor
        )
        if (secondaryText != null) {
          Spacer(modifier = Modifier.height(2.dp))
          Text(
            text = secondaryText,
            style = MaterialTheme.typography.bodySmall,
            color = MaterialTheme.colorScheme.onSurfaceVariant
          )
        }
      }

      IconButton(
        onClick = onCopy,
        modifier = Modifier.testTag("copy_result_button")
      ) {
        Icon(
          imageVector = Icons.Default.ContentCopy,
          contentDescription = "Copy Result",
          tint = MaterialTheme.colorScheme.primary
        )
      }
    }
  }
}

private fun copyToClipboard(context: Context, text: String) {
  val clipboard = context.getSystemService(Context.CLIPBOARD_SERVICE) as ClipboardManager
  val clip = ClipData.newPlainText("Calculation Result", text)
  clipboard.setPrimaryClip(clip)
  Toast.makeText(context, "Copied: $text", Toast.LENGTH_SHORT).show()
}
